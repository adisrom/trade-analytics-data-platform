CREATE OR REPLACE VIEW trade.supplier_risk_distribution AS

SELECT

    risk_category,

    COUNT(*) AS supplier_count,

    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_of_suppliers


FROM trade.supplier_risk_score

GROUP BY
    risk_category

ORDER BY
    supplier_count DESC;