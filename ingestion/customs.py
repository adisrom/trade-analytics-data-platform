import random
import pandas as pd

from ingestion.database import get_engine


def generate_customs_entries():
    """
    Generate customs declarations based on shipments.
    """

    engine = get_engine()

    shipments = pd.read_sql(
        """
        SELECT 
            s.shipment_id,
            p.hts_code,
            p.unit_value,
            s.quantity
        FROM trade.shipments s
        JOIN trade.products p
        ON s.product_id = p.product_id
        """,
        engine
    )

    duty_rates = {
        "8471.30": 0.05,   # Electronics
        "8517.62": 0.05,
        "8517.13": 0.05,
        "9031.80": 0.08,
        "9018.90": 0.03,
        "8708.99": 0.08,
        "8507.60": 0.06
    }

    statuses = [
        "Cleared",
        "Pending Review",
        "Hold",
        "Rejected"
    ]

    customs_entries = []

    for _, shipment in shipments.iterrows():

        declared_value = (
            shipment["quantity"] *
            shipment["unit_value"]
        )

        duty_rate = duty_rates.get(
            shipment["hts_code"],
            0.05
        )

        duty_amount = declared_value * duty_rate

        customs_entries.append({
            "shipment_id": shipment["shipment_id"],
            "hts_code": shipment["hts_code"],
            "declared_value": round(declared_value, 2),
            "duty_amount": round(duty_amount, 2),
            "clearance_status": random.choice(statuses)
        })

    return pd.DataFrame(customs_entries)


def load_customs_entries(df):
    """
    Load customs entries into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        "customs_entries",
        engine,
        schema="trade",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} customs entries")