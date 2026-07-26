# Trade Analytics Data Dictionary

## suppliers

Stores supplier/company information.

| Column | Description |
|---|---|
| supplier_id | Unique supplier identifier |
| supplier_name | Supplier company name |
| country | Supplier country |
| risk_rating | Compliance risk classification |
| created_at | Record creation timestamp |


## products

Stores product classification information.

| Column | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product description |
| hts_code | Harmonized Tariff Schedule classification |
| category | Product category |
| unit_value | Unit value of product |


## shipments

Stores shipment movement events.

| Column | Description |
|---|---|
| shipment_id | Unique shipment identifier |
| supplier_id | Related supplier |
| product_id | Related product |
| origin_country | Country goods shipped from |
| destination_country | Country goods shipped to |
| departure_date | Shipment departure date |
| arrival_date | Shipment arrival date |
| shipment_status | Current shipment status |
| quantity | Number of units shipped |


## customs_entries

Stores customs declaration information.

| Column | Description |
|---|---|
| entry_id | Unique customs entry |
| shipment_id | Related shipment |
| hts_code | Tariff classification |
| declared_value | Declared customs value |
| duty_amount | Duty paid |
| clearance_status | Customs clearance result |


## inspections

Stores inspection events.

| Column | Description |
|---|---|
| inspection_id | Unique inspection identifier |
| shipment_id | Related shipment |
| inspection_date | Inspection date |
| inspection_type | Type of inspection |
| result | Inspection outcome |