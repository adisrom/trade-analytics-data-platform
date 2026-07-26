CREATE OR REPLACE VIEW trade.supplier_risk_summary AS

SELECT
    s.supplier_id,
    s.supplier_name,
    s.country,
    s.risk_rating,

    COUNT(DISTINCT sh.shipment_id) AS total_shipments,

    COUNT(DISTINCT i.inspection_id) AS total_inspections,

    SUM(
        CASE 
            WHEN i.result = 'Failed'
            THEN 1
            ELSE 0
        END
    ) AS failed_inspections,

    ROUND(
        AVG(
            CASE
                WHEN i.result = 'Failed'
                THEN 1
                ELSE 0
            END
        ) * 100,
        2
    ) AS failure_rate_percentage,

    SUM(c.duty_amount) AS total_duty_exposure

FROM trade.suppliers s

JOIN trade.shipments sh
ON s.supplier_id = sh.supplier_id

LEFT JOIN trade.customs_entries c
ON sh.shipment_id = c.shipment_id

LEFT JOIN trade.inspections i
ON sh.shipment_id = i.shipment_id

GROUP BY
    s.supplier_id,
    s.supplier_name,
    s.country,
    s.risk_rating;