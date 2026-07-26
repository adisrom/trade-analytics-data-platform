import random
import pandas as pd
from faker import Faker

from ingestion.database import get_engine


fake = Faker()


def generate_inspections():
    """
    Generate synthetic inspection records based on shipments.
    """

    engine = get_engine()

    shipments = pd.read_sql(
        """
        SELECT shipment_id
        FROM trade.shipments
        """,
        engine
    )

    inspection_types = [
        "Customs Audit",
        "Document Review",
        "Physical Inspection",
        "Compliance Check"
    ]

    results = [
        "Passed",
        "Flagged",
        "Failed"
    ]

    inspections = []

    for _, shipment in shipments.iterrows():

        inspections.append({
            "shipment_id": shipment["shipment_id"],
            "inspection_date": fake.date_between(
                start_date="-1y",
                end_date="today"
            ),
            "inspection_type": random.choice(
                inspection_types
            ),
            "result": random.choice(
                results
            )
        })

    return pd.DataFrame(inspections)


def load_inspections(df):
    """
    Load inspection records into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        "inspections",
        engine,
        schema="trade",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} inspections")