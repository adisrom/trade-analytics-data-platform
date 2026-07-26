CREATE OR REPLACE VIEW trade.supplier_risk_score AS

WITH supplier_metrics AS (

    SELECT
        supplier_id,
        supplier_name,
        country,
        risk_rating,
        failure_rate_percentage,
        total_duty_exposure,
        failure_rate_percentage,
     failed_inspections,
     total_inspections,
     total_shipments,
     total_duty_exposure

        MAX(total_duty_exposure)
        OVER () AS max_duty

    FROM trade.supplier_risk_summary

)

SELECT

    supplier_id,
    supplier_name,
    country,

    ROUND(
        (
            failure_rate_percentage * 0.5
        )
        +
        (
            (total_duty_exposure / NULLIF(max_duty,0)) * 25
        )
        +
        (
            CASE
                WHEN risk_rating = 'High'
                    THEN 25
                WHEN risk_rating = 'Medium'
                    THEN 15
                ELSE 5
            END
        ),
        2
    ) AS risk_score,


    CASE

        WHEN
            (
                (failure_rate_percentage * 0.5)
                +
                ((total_duty_exposure / NULLIF(max_duty,0)) * 25)
                +
                (
                    CASE
                        WHEN risk_rating = 'High'
                            THEN 25
                        WHEN risk_rating = 'Medium'
                            THEN 15
                        ELSE 5
                    END
                )
            ) >= 60

        THEN 'High'


        WHEN
            (
                (failure_rate_percentage * 0.5)
                +
                ((total_duty_exposure / NULLIF(max_duty,0)) * 25)
                +
                (
                    CASE
                        WHEN risk_rating = 'High'
                            THEN 25
                        WHEN risk_rating = 'Medium'
                            THEN 15
                        ELSE 5
                    END
                )
            ) >= 30

        THEN 'Medium'

        ELSE 'Low'

    END AS risk_category


FROM supplier_metrics;