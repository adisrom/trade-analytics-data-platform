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

if __name__ == "__main__":

    suppliers_df = generate_suppliers(100)
    load_suppliers(suppliers_df)

    products_df = generate_products(100)
    load_products(products_df)

    shipments_df = generate_shipments(1000)
    load_shipments(shipments_df)