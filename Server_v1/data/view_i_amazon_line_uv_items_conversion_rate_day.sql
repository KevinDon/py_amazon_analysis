-- amazon analysis buy box stat
-- REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_items_conversion_rate_day;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_line_uv_items_conversion_rate_day;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_line_uv_items_conversion_rate_day" AS
    SELECT row_number() OVER () AS id,
        main.title,
        main.line_id,
        main.dy,
        COALESCE((counts.num)::real, (0)::real) AS num
       FROM (( SELECT line.title,
                line.id AS line_id,
                psd.date_day AS dy
               FROM na_product_line line,
                pub_stat_days psd) main
         LEFT JOIN ( SELECT repo.line_id,
                repo.dy,
                    CASE
                        WHEN (sum(repo.sessions) = 0) THEN ((0)::bigint)::double precision
                        ELSE (round(((sum(repo.total_order_items))::numeric / (sum(repo.sessions))::numeric), 2))::double precision
                    END AS num
               FROM ( SELECT rp.sessions,
                        rp.total_order_items,
                        pro.line_id,
                        (rp.report_date)::date AS dy
                       FROM ((na_business_report rp
                         LEFT JOIN na_product_asin pro ON (((rp.asin_child)::text = (pro.asin)::text)))
                         LEFT JOIN na_product_line line ON ((line.id = pro.line_id)))) repo
              GROUP BY repo.line_id, repo.dy) counts(line_id, dy, num) ON ((((counts.line_id)::text = (main.line_id)::text) AND (counts.dy = main.dy))))
      ORDER BY main.line_id
;
