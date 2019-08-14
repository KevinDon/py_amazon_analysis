
-- DROP VIEW IF EXISTS view_i_amazon_sku_review;
CREATE VIEW "public"."view_i_amazon_sku_review" AS  SELECT sku.sku,
    sku.asin,
    sku.line_id,
    review.id,
    review.review_at,
    review.review_rank,
    review.link,
    review.author,
    review.title,
    review.content,
    review.selection,
    review.platform
   FROM (amazon_capture_sku_review review
     LEFT JOIN na_product_asin sku ON (((review.asin)::text = (sku.asin)::text)));
