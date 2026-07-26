CREATE OR REPLACE VIEW trade.customs_duty_summary AS

SELECT

    s.origin_country,

    p.category,

    COUNT(DISTINCT s.shipment_id) AS total_shipments,

    SUM(s.quantity) AS total_units,

    SUM(c.declared_value) AS total_declared_value,

    SUM(c.duty_amount) AS total_duty_amount,

    ROUND(
        SUM(c.duty_amount) /
        NULLIF(SUM(c.declared_value), 0) * 100,
        2
    ) AS effective_duty_rate_percentage


FROM trade.shipments s

JOIN trade.products p
ON s.product_id = p.product_id

JOIN trade.customs_entries c
ON s.shipment_id = c.shipment_id


GROUP BY

    s.origin_country,
    p.category;