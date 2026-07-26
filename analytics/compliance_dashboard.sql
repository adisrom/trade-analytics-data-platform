CREATE OR REPLACE VIEW trade.compliance_dashboard_summary AS

SELECT

    COUNT(DISTINCT sh.shipment_id) AS total_shipments,

    SUM(c.declared_value) AS total_trade_value,

    SUM(c.duty_amount) AS total_duty_exposure,

    COUNT(DISTINCT s.supplier_id) AS total_suppliers,

    COUNT(
        DISTINCT CASE
            WHEN r.risk_category = 'High'
            THEN r.supplier_id
        END
    ) AS high_risk_suppliers,

    ROUND(
        AVG(
            CASE
                WHEN i.result = 'Failed'
                THEN 1
                ELSE 0
            END
        ) * 100,
        2
    ) AS inspection_failure_rate_percentage


FROM trade.shipments sh

JOIN trade.customs_entries c
ON sh.shipment_id = c.shipment_id

JOIN trade.suppliers s
ON sh.supplier_id = s.supplier_id

LEFT JOIN trade.inspections i
ON sh.shipment_id = i.shipment_id

LEFT JOIN trade.supplier_risk_score r
ON s.supplier_id = r.supplier_id;