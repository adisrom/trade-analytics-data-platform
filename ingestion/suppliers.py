from faker import Faker
import random
import pandas as pd

from ingestion.database import get_engine


fake = Faker()


def generate_suppliers(num_suppliers=100):
    """
    Generate synthetic supplier records.
    """

    countries = [
        "China",
        "India",
        "Germany",
        "Japan",
        "Mexico",
        "Vietnam",
        "United States"
    ]

    risk_levels = [
        "Low",
        "Medium",
        "High"
    ]

    suppliers = []

    for i in range(num_suppliers):
        suppliers.append({
            "supplier_name": fake.company(),
            "country": random.choice(countries),
            "risk_rating": random.choice(risk_levels)
        })

    return pd.DataFrame(suppliers)


def load_suppliers(df):
    """
    Load supplier data into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        "suppliers",
        engine,
        schema="trade",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} suppliers")