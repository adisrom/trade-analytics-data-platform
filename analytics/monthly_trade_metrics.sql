CREATE OR REPLACE VIEW trade.monthly_trade_metrics AS

SELECT

    DATE_TRUNC('month', sh.departure_date)::date AS month,

    COUNT(DISTINCT sh.shipment_id) AS total_shipments,

    SUM(c.declared_value) AS total_declared_value,

    SUM(c.duty_amount) AS total_duty_amount,

   ROUND(
    AVG(
        c.duty_amount / NULLIF(c.declared_value,0)
    ) * 100,
    2
) AS average_duty_rate_percentage

FROM trade.shipments sh

JOIN trade.customs_entries c
ON sh.shipment_id = c.shipment_id


GROUP BY
    DATE_TRUNC('month', sh.departure_date)


ORDER BY
    month;