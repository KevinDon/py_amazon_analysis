-- amazon analysis user view stat
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_day;
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_month;
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_week;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_line_uv_day;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_line_uv_day" AS
    SELECT row_number() OVER () AS id,
        main.title,
        main.line_id,
        main.dy,
        COALESCE(counts.num, (0)::bigint) AS num
       FROM (( SELECT line.title,
                line.id AS line_id,
                psd.date_day AS dy
               FROM na_product_line line,
                pub_stat_days psd) main
         LEFT JOIN ( SELECT repo.line_id,
                repo.dy,
                sum(repo.sessions) AS num
               FROM ( SELECT pro.line_id,
                        rp.sessions,
                        (rp.report_date)::date AS dy
                       FROM ((na_business_report rp
                         LEFT JOIN na_product_asin pro ON (((rp.asin_child)::text = (pro.asin)::text)))
                         LEFT JOIN na_product_line line ON ((line.id = pro.line_id)))) repo
              GROUP BY repo.line_id, repo.dy) counts ON ((((counts.line_id)::text = (main.line_id)::text) AND (counts.dy = main.dy))))
  ORDER BY main.line_id
;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_line_uv_month;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_line_uv_month" AS
    SELECT row_number() OVER () AS id,
        main.title,
        main.line_id,
        main.yr,
        main.mo,
        main.first_day,
        main.last_day,
        COALESCE(counts.num, (0)::bigint) AS num
       FROM (( SELECT line.title,
                line.id AS line_id,
                psm.yr,
                psm.mo,
                psm.first_day,
                psm.last_day
               FROM na_product_line line,
                pub_stat_month psm) main
         LEFT JOIN ( SELECT repo.line_id,
                repo.yr,
                repo.mo,
                sum(repo.sessions) AS num
               FROM ( SELECT pro.line_id,
                        rp.sessions,
                        date_part('year'::text, rp.report_date) AS yr,
                        date_part('month'::text, rp.report_date) AS mo
                       FROM ((na_business_report rp
                         LEFT JOIN na_product_asin pro ON (((rp.asin_child)::text = (pro.asin)::text)))
                         LEFT JOIN na_product_line line ON ((line.id = pro.line_id)))) repo
              GROUP BY repo.line_id, repo.yr, repo.mo) counts ON ((((counts.line_id)::text = (main.line_id)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.mo = (main.mo)::double precision))))
  ORDER BY main.line_id
;
	
	

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_line_uv_week;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_line_uv_week" AS
     SELECT row_number() OVER () AS id,
        main.title,
        main.line_id,
        main.yr,
        main.wk,
        main.first_day,
        main.last_day,
        COALESCE(counts.num, (0)::bigint) AS num
       FROM (( SELECT line.title,
                line.id AS line_id,
                psw.yr,
                psw.wk,
                psw.first_day,
                psw.last_day
               FROM na_product_line line,
                pub_stat_weeks psw) main
         LEFT JOIN ( SELECT repo.line_id,
                repo.yr,
                repo.wk,
                sum(repo.sessions) AS num
               FROM ( SELECT pro.line_id,
                        rp.sessions,
                        date_part('year'::text, ((rp.report_date)::date + 1)) AS yr,
                        date_part('week'::text, ((rp.report_date)::date + 1)) AS wk
                       FROM ((na_business_report rp
                         LEFT JOIN na_product_asin pro ON (((rp.asin_child)::text = (pro.asin)::text)))
                         LEFT JOIN na_product_line line ON ((line.id = pro.line_id)))) repo
              GROUP BY repo.line_id, repo.yr, repo.wk) counts ON ((((counts.line_id)::text = (main.line_id)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
      ORDER BY main.line_id
;
	
