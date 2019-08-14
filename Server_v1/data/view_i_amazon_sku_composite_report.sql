-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_composite_report_day;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_composite_report_day"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.dy,
    COALESCE(counts.uv_num, (0)::bigint) AS uv_num,
    COALESCE(counts.total_order_items_num, (0)::bigint) AS total_order_items_num,
    COALESCE(counts.pv_num, (0)::bigint) AS pv_num,
    COALESCE(counts.buy_box_per_num, ((0)::bigint)::real) AS buy_box_per_num
   FROM (( SELECT skus.sku,
            skus.asin,
            psd.date_day AS dy
           FROM na_product_asin skus,
            pub_stat_days psd) main
     LEFT JOIN ( SELECT repo.asin,
            repo.dy,
            sum(repo.sessions) AS uv_num,
            sum(repo.total_order_items) AS total_order_items_num,
            sum(repo.page_view) AS pv_num,
            min(repo.buy_box_percentage) AS buy_box_per_num
           FROM ( SELECT na_business_report.asin_child AS asin,
                    na_business_report.sessions,
                    na_business_report.total_order_items,
                    na_business_report.page_view,
                    na_business_report.buy_box_percentage,
                    (na_business_report.report_date)::date AS dy
                   FROM na_business_report) repo
          GROUP BY repo.asin, repo.dy) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.dy = main.dy))))
  ORDER BY main.sku;
  
 
 -- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_composite_report_month;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_composite_report_month"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.yr,
    main.mo,
    main.first_day,
    main.last_day,
    COALESCE(counts.uv_num, (0)::bigint) AS uv_num,
    COALESCE(counts.total_order_items_num, (0)::bigint) AS total_order_items_num,
    COALESCE(counts.pv_num, (0)::bigint) AS pv_num,
    COALESCE(counts.buy_box_per_num, (((0)::bigint)::real)::double precision) AS buy_box_per_num
   FROM (( SELECT skus.sku,
            skus.asin,
            psm.yr,
            psm.mo,
            psm.first_day,
            psm.last_day
           FROM na_product_asin skus,
            pub_stat_month psm) main
     LEFT JOIN ( SELECT repo.asin,
            repo.yr,
            repo.mo,
            sum(repo.sessions) AS uv_num,
            sum(repo.total_order_items) AS total_order_items_num,
            sum(repo.page_view) AS pv_num,
            avg(repo.buy_box_percentage) AS buy_box_per_num
           FROM ( SELECT na_business_report.asin_child AS asin,
                    na_business_report.sessions,
                    na_business_report.total_order_items,
                    na_business_report.page_view,
                    na_business_report.buy_box_percentage,
                    date_part('year'::text, na_business_report.report_date) AS yr,
                    date_part('month'::text, na_business_report.report_date) AS mo
                   FROM na_business_report) repo
          GROUP BY repo.asin, repo.yr, repo.mo) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.mo = (main.mo)::double precision))))
  ORDER BY main.sku;


 -- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_composite_report_week;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_composite_report_week"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.yr,
    main.wk,
    main.first_day,
    main.last_day,
    COALESCE(counts.uv_num, (0)::bigint) AS uv_num,
    COALESCE(counts.total_order_items_num, (0)::bigint) AS total_order_items_num,
    COALESCE(counts.pv_num, (0)::bigint) AS pv_num,
    COALESCE(counts.buy_box_per_num, (((0)::bigint)::real)::double precision) AS buy_box_per_num
   FROM (( SELECT skus.sku,
            skus.asin,
            psw.yr,
            psw.wk,
            psw.first_day,
            psw.last_day
           FROM na_product_asin skus,
            pub_stat_weeks psw) main
     LEFT JOIN ( SELECT repo.asin,
            repo.yr,
            repo.wk,
            sum(repo.sessions) AS uv_num,
            sum(repo.total_order_items) AS total_order_items_num,
            sum(repo.page_view) AS pv_num,
            avg(repo.buy_box_percentage) AS buy_box_per_num
           FROM ( SELECT na_business_report.asin_child AS asin,
                    na_business_report.sessions,
                    na_business_report.total_order_items,
                    na_business_report.page_view,
                    na_business_report.buy_box_percentage,
                    date_part('year'::text, ((na_business_report.report_date)::date + 1)) AS yr,
                    date_part('week'::text, ((na_business_report.report_date)::date + 1)) AS wk
                   FROM na_business_report) repo
          GROUP BY repo.asin, repo.yr, repo.wk) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
  ORDER BY main.sku;

ALTER MATERIALIZED VIEW "public"."view_i_amazon_sku_composite_report_week" OWNER TO "postgres";