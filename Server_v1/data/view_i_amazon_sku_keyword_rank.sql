-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_keyword_rank_day;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_keyword_rank_day"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    main.sku_keyword_id,
    main.dy,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((skus.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            psd.date_day AS dy
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.sku_keyword_id
                   FROM amazon_capture_sku_keyword_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.sku_keyword_id) skus,
            pub_stat_days psd) main
     LEFT JOIN ( SELECT repo.asin,
            repo.dy,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((repo.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            round(avg(repo.rank_on)) AS num
           FROM ( SELECT rp.asin,
                    rp.sku_keyword_id,
                    rp.category_id,
                    rp.rank_on,
                    (rp.capture_at)::date AS dy
                   FROM amazon_capture_sku_keyword_rank rp) repo
          GROUP BY repo.asin, repo.dy, repo.category_id, repo.sku_keyword_id) counts ON ((((counts.asin)::text = (main.asin)::text) AND ((counts.dy)::text = (main.dy)::text) AND (counts.category_id = main.category_id) AND (counts.sku_keyword_id = main.sku_keyword_id))))
  ORDER BY main.asin

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_keyword_rank_month;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_keyword_rank_month"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    counts.sku_keyword_id,
    main.yr,
    main.wk,
    main.first_day,
    main.last_day,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((skus.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            psw.yr,
            psw.wk,
            psw.first_day,
            psw.last_day
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.sku_keyword_id
                   FROM amazon_capture_sku_keyword_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.sku_keyword_id) skus,
            pub_stat_weeks psw) main
     LEFT JOIN ( SELECT repo.asin,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((repo.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            round(avg(repo.rank_on)) AS num,
            repo.yr,
            repo.wk
           FROM ( SELECT rp.asin,
                    rp.sku_keyword_id,
                    rp.category_id,
                    rp.rank_on,
                    date_part('year'::text, ((rp.capture_at)::date + 1)) AS yr,
                    date_part('week'::text, ((rp.capture_at)::date + 1)) AS wk
                   FROM amazon_capture_sku_keyword_rank rp) repo
          GROUP BY repo.asin, repo.yr, repo.wk, repo.category_id, repo.sku_keyword_id) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.category_id = main.category_id) AND (counts.sku_keyword_id = main.sku_keyword_id) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
  ORDER BY main.asin

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_keyword_rank_week;
CREATE MATERIALIZED VIEW "public"."view_i_amazon_sku_keyword_rank_week"
AS
SELECT row_number() OVER () AS id,
    main.sku,
    main.asin,
    main.category_id,
    counts.sku_keyword_id,
    main.yr,
    main.wk,
    main.first_day,
    main.last_day,
    COALESCE((counts.num)::bigint, (0)::bigint) AS num
   FROM (( SELECT skus.sku,
            skus.asin,
            COALESCE((skus.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((skus.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            psw.yr,
            psw.wk,
            psw.first_day,
            psw.last_day
           FROM ( SELECT repo.sku,
                    repo.asin,
                    repo.category_id,
                    repo.sku_keyword_id
                   FROM amazon_capture_sku_keyword_rank repo
                  GROUP BY repo.sku, repo.asin, repo.category_id, repo.sku_keyword_id) skus,
            pub_stat_weeks psw) main
     LEFT JOIN ( SELECT repo.asin,
            COALESCE((repo.category_id)::bigint, (0)::bigint) AS category_id,
            COALESCE((repo.sku_keyword_id)::bigint, (0)::bigint) AS sku_keyword_id,
            round(avg(repo.rank_on)) AS num,
            repo.yr,
            repo.wk
           FROM ( SELECT rp.asin,
                    rp.sku_keyword_id,
                    rp.category_id,
                    rp.rank_on,
                    date_part('year'::text, ((rp.capture_at)::date + 1)) AS yr,
                    date_part('week'::text, ((rp.capture_at)::date + 1)) AS wk
                   FROM amazon_capture_sku_keyword_rank rp) repo
          GROUP BY repo.asin, repo.yr, repo.wk, repo.category_id, repo.sku_keyword_id) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.category_id = main.category_id) AND (counts.sku_keyword_id = main.sku_keyword_id) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
  ORDER BY main.asin
