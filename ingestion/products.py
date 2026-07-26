import random
import pandas as pd

from ingestion.database import get_engine


def generate_products(num_products=100):
    """
    Generate synthetic product records.
    """

    products = []

    product_catalog = [
        ("Laptop Computer", "8471.30", "Electronics"),
        ("Wireless Router", "8517.62", "Networking"),
        ("Industrial Sensor", "9031.80", "Manufacturing"),
        ("Mobile Phone", "8517.13", "Electronics"),
        ("Medical Device", "9018.90", "Healthcare"),
        ("Automotive Component", "8708.99", "Automotive"),
        ("Battery Module", "8507.60", "Energy")
    ]

    for i in range(num_products):

        product = random.choice(product_catalog)

        products.append({
            "product_name": product[0],
            "hts_code": product[1],
            "category": product[2],
            "unit_value": round(random.uniform(10, 2000), 2)
        })

    return pd.DataFrame(products)


def load_products(df):
    """
    Load product data into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        "products",
        engine,
        schema="trade",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} products")