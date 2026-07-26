from ingestion.suppliers import (
    generate_suppliers,
    load_suppliers
)

from ingestion.products import (
    generate_products,
    load_products
)

from ingestion.shipments import (
    generate_shipments,
    load_shipments
)

from ingestion.customs import (
    generate_customs_entries,
    load_customs_entries
)

def run_pipeline():
    """
    Runs the complete trade data ingestion pipeline.
    """

    print("Starting trade analytics pipeline...")


    # Step 1: Generate and load suppliers
    suppliers_df = generate_suppliers(100)
    load_suppliers(suppliers_df)


    # Step 2: Generate and load products
    products_df = generate_products(100)
    load_products(products_df)


    # Step 3: Generate and load shipments
    shipments_df = generate_shipments(1000)
    load_shipments(shipments_df)

     # Step 4: Generate and load customs entries
    customs_df = generate_customs_entries()
    load_customs_entries(customs_df)


    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()