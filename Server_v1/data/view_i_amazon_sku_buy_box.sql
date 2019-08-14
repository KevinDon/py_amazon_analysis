-- amazon analysis buy box stat
-- REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_buy_box_day;


-- DROP MATERIALIZED VIEW IF EXISTS view_i_amazon_sku_buy_box_day;
CREATE MATERIALIZED VIEW IF NOT EXISTS "public"."view_i_amazon_sku_buy_box_day" AS
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
				min(buy_box_percentage) AS num
			 FROM (
					SELECT
						asin_child as asin,
						buy_box_percentage,
						report_date::date AS dy
					FROM na_business_report
				) repo
				GROUP BY repo.asin, repo.dy
			) counts ON counts.asin = main.asin and counts.dy=main.dy
	ORDER BY main.sku
;
