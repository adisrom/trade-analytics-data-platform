import random
import pandas as pd
from faker import Faker

from ingestion.database import get_engine


fake = Faker()


def generate_shipments(num_shipments=1000):
    """
    Generate synthetic shipment records.
    """

    engine = get_engine()

    suppliers = pd.read_sql(
        "SELECT supplier_id, country FROM trade.suppliers",
        engine
    )

    products = pd.read_sql(
        "SELECT product_id FROM trade.products",
        engine
    )

    statuses = [
        "Pending",
        "In Transit",
        "Customs Hold",
        "Cleared",
        "Delivered"
    ]

    shipments = []

    for i in range(num_shipments):

        supplier = suppliers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]

        departure_date = fake.date_between(
            start_date="-1y",
            end_date="today"
        )

        arrival_date = fake.date_between(
            start_date=departure_date,
            end_date="today"
        )

        shipments.append({
            "supplier_id": supplier["supplier_id"],
            "product_id": product["product_id"],
            "origin_country": supplier["country"],
            "destination_country": "United States",
            "departure_date": departure_date,
            "arrival_date": arrival_date,
            "shipment_status": random.choice(statuses),
            "quantity": random.randint(10, 1000)
        })

    return pd.DataFrame(shipments)


def load_shipments(df):
    """
    Load shipment data into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        "shipments",
        engine,
        schema="trade",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} shipments")