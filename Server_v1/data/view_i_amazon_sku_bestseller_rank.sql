-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_bestseller_rank_day;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_bestseller_rank_day"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    main.category_title,
    main.dy,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            skus.category_title,
            psd.date_day AS dy
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.category_title
                   FROM amazon_capture_sku_bestseller_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.category_title) skus,
            pub_stat_days psd) main
     LEFT JOIN ( SELECT repo.asin,
            repo.dy,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            round(avg(repo.rank_on)) AS num
           FROM ( SELECT rp.asin,
                    rp.category_id,
                    rp.rank_on,
                    (rp.capture_at)::date AS dy
                   FROM amazon_capture_sku_bestseller_rank rp) repo
          GROUP BY repo.asin, repo.dy, repo.category_id) counts ON ((((counts.asin)::text = (main.asin)::text) AND ((counts.dy)::text = (main.dy)::text) AND (counts.category_id = main.category_id))))
  ORDER BY main.asin;

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_bestseller_rank_month;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_bestseller_rank_month"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    main.category_title,
    main.yr,
    main.mo,
    main.first_day,
    main.last_day,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            skus.category_title,
            psm.yr,
            psm.mo,
            psm.first_day,
            psm.last_day
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.category_title
                   FROM amazon_capture_sku_bestseller_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.category_title) skus,
            pub_stat_month psm) main
     LEFT JOIN ( SELECT repo.asin,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            round(avg(repo.rank_on)) AS num,
            repo.yr,
            repo.mo
           FROM ( SELECT rp.asin,
                    rp.category_id,
                    rp.rank_on,
                    date_part('year'::text, rp.capture_at) AS yr,
                    date_part('month'::text, rp.capture_at) AS mo
                   FROM amazon_capture_sku_bestseller_rank rp) repo
          GROUP BY repo.asin, repo.category_id, repo.yr, repo.mo) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.category_id = main.category_id) AND (counts.yr = (main.yr)::double precision) AND (counts.mo = (main.mo)::double precision))))
  ORDER BY main.asin;

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_bestseller_rank_week;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_bestseller_rank_week"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    main.category_title,
    main.yr,
    main.wk,
    main.first_day,
    main.last_day,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            skus.category_title,
            psw.yr,
            psw.wk,
            psw.first_day,
            psw.last_day
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.category_title
                   FROM amazon_capture_sku_bestseller_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.category_title) skus,
            pub_stat_weeks psw) main
     LEFT JOIN ( SELECT repo.asin,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            round(avg(repo.rank_on)) AS num,
            repo.yr,
            repo.wk
           FROM ( SELECT rp.asin,
                    rp.category_id,
                    rp.rank_on,
                    date_part('year'::text, ((rp.capture_at)::date + 1)) AS yr,
                    date_part('week'::text, ((rp.capture_at)::date + 1)) AS wk
                   FROM amazon_capture_sku_bestseller_rank rp) repo
          GROUP BY repo.asin, repo.yr, repo.wk, repo.category_id) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.category_id = main.category_id) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
  ORDER BY main.asin;
