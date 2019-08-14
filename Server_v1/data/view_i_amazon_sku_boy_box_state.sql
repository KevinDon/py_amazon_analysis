
-- DROP VIEW IF EXISTS view_i_amazon_sku_boy_box_state;
CREATE VIEW "public"."view_i_amazon_sku_boy_box_state" AS  SELECT sku.sku,
    sku.asin,
    sku.line_id,
    buybox.id,
    buybox.buy_box_state,
    buybox.capture_at,
    buybox.link,
    buybox.sold_by,
    buybox.sold_by_price,
    buybox.platform
   FROM (amazon_capture_sku_buy_box_state buybox
     LEFT JOIN na_product_asin sku ON (((buybox.asin)::text = (sku.asin)::text)));
