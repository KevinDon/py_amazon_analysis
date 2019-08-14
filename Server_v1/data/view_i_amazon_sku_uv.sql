-- amazon analysis user view stat
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_day;
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_month;
--REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_week;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_uv_day;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_sku_uv_day" AS
	SELECT
		row_number() OVER () AS id
		, main.sku
		, main.asin
		, main.dy
		, COALESCE (counts.num, 0) as num
		FROM (
			select
			skus.sku
			, skus.asin
			, psd.date_day as dy
			FROM na_product_asin skus, pub_stat_days psd
		) main
		LEFT JOIN(
			SELECT 
				repo.asin,
				repo.dy,
				sum(sessions) AS num
			 FROM (
					SELECT
						asin_child as asin,
						sessions,
						report_date::date AS dy
					FROM na_business_report
				) repo
				GROUP BY repo.asin, repo.dy
			) counts ON counts.asin = main.asin and counts.dy=main.dy
	ORDER BY main.sku
;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_uv_month;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_sku_uv_month" AS
	SELECT
		row_number() OVER () AS id
		, main.sku
		, main.asin
		, main.yr
		, main.mo
		, main.first_day
		, main.last_day
		, COALESCE (counts.num, 0) as num
		FROM (
			select
			skus.sku
			, skus.asin
			, psm.yr as yr
			, psm.mo as mo
			, psm.first_day as first_day
			, psm.last_day as last_day
			FROM na_product_asin skus, pub_stat_month psm
		) main
		LEFT JOIN(
			SELECT 
				repo.asin,
				repo.yr,
				repo.mo,
				sum(repo.sessions) AS num
			 FROM (
					SELECT
						asin_child as asin,
						sessions,
						date_part('year'::text, report_date) AS yr,
						date_part('month'::text, report_date) AS mo
					FROM na_business_report
				) repo
				GROUP BY repo.asin, repo.yr, repo.mo
			) counts ON counts.asin = main.asin and counts.yr=main.yr and counts.mo=main.mo
	ORDER BY main.sku
;
	
	

-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_uv_week;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_sku_uv_week" AS
    SELECT row_number() OVER () AS id,
        main.sku,
        main.asin,
        main.yr,
        main.wk,
        main.first_day,
        main.last_day,
        COALESCE(counts.num, (0)::bigint) AS num
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
                sum(repo.sessions) AS num
               FROM ( SELECT na_business_report.asin_child AS asin,
                        na_business_report.sessions,
                        date_part('year'::text, ((na_business_report.report_date)::date + 1)) AS yr,
                        date_part('week'::text, ((na_business_report.report_date)::date + 1)) AS wk
                       FROM na_business_report) repo
              GROUP BY repo.asin, repo.yr, repo.wk) counts ON ((((counts.asin)::text = (main.asin)::text) AND (counts.yr = (main.yr)::double precision) AND (counts.wk = (main.wk)::double precision))))
      ORDER BY main.sku
;
	
