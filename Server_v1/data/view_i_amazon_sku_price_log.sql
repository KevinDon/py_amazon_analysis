-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_price_log_day;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_price_log_day"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.dy,
    COALESCE(counts.price, (0)::double precision) AS price
   FROM (( SELECT skus.sku,
            skus.asin,
            psd.date_day AS dy
           FROM na_product_asin skus,
            pub_stat_days psd) main
     LEFT JOIN ( SELECT repo.asin,
            repo.dy,
            avg((repo.price)::double precision) AS price
           FROM ( SELECT rp.asin,
                    rp.price,
                    (rp.capture_at)::date AS dy
                   FROM amazon_capture_sku_price rp) repo
          GROUP BY repo.asin, repo.dy) counts ON ((((counts.asin)::text = (main.asin)::text) AND ((counts.dy)::text = (main.dy)::text))))
  ORDER BY main.sku
;

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_price_log_month;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_price_log_month"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.yr,
    main.mo,
    main.first_day,
    main.last_day,
    COALESCE(counts.price, (0)::double precision) AS price
   FROM (( SELECT skus.sku,
            skus.asin,
            psm.yr,
            psm.mo,
            psm.first_day,
            psm.last_day
           FROM na_product_asin skus,
            pub_stat_month psm) main
     LEFT JOIN ( SELECT repo.asin,
            avg((repo.price)::double precision) AS price,
            repo.yr,
            repo.mo
           FROM ( SELECT rp.asin,
                    rp.price,
                    date_part('year'::text, rp.capture_at) AS yr,
                    date_part('month'::text, rp.capture_at) AS mo
                   FROM amazon_capture_sku_price rp) repo
          GROUP BY repo.asin, repo.yr, repo.mo) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.mo = (main.mo)::double precision))))
  ORDER BY main.asin
;

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_price_log_week;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_price_log_week"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.yr,
    main.wk,
    main.first_day,
    main.last_day,
    COALESCE(counts.price, (0)::double precision) AS price
   FROM (( SELECT skus.sku,
            skus.asin,
            psw.yr,
            psw.wk,
            psw.first_day,
            psw.last_day
           FROM na_product_asin skus,
            pub_stat_weeks psw) main
     LEFT JOIN ( SELECT repo.asin,
            avg((repo.price)::double precision) AS price,
            repo.yr,
            repo.wk
           FROM ( SELECT rp.asin,
                    rp.price,
                    date_part('year'::text, ((rp.capture_at)::date + 1)) AS yr,
                    date_part('week'::text, ((rp.capture_at)::date + 1)) AS wk
                   FROM amazon_capture_sku_price rp) repo
          GROUP BY repo.asin, repo.yr, repo.wk) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
  ORDER BY main.asin
;