# Data Modeling Philosophy

This project follows an analytics engineering approach, emphasizing:
* Clear separation of data layers.
* Explicit control of metric definitions.
* Looker Studio–ready semantic modeling.
* Avoidance of dashboard-level blending or calculated field complexity.

## Layered Data Architecture

### 1. Raw Fact Layer
**Table:** `driiiportfolio.raw.fact_product_metrics`
* **Purpose:** Store daily, product-level operational and financial metrics; preserve maximum granularity for flexibility and auditability.
* **Grain:** One row per `product_id` per `date`.

### 2. Staging Layer
**View:** `driiiportfolio.raw.stg_product_metrics`
* **Purpose:** Clean and standardize raw metrics; enforce basic data validity (e.g., exclude null yield values).
* **Key Transformations:** Safe division for demand accuracy; removal of invalid or incomplete quality records.

### 3. Analytics / Semantic Layer
**View:** `driiiportfolio.analytics.product_daily_semantic`
* **Purpose:** Serve as the primary Looker Studio data source; preserve daily grain while exposing analytics-ready fields.
* **Functionality:** Enables time-series analysis, scatter plots, and operational diagnostics without Looker blends.

### 4. Aggregated Summary Layer
**View:** `driiiportfolio.raw.product_performance_summary`
* **Purpose:** Provide product-level rollups for executive KPIs; optimize performance for summary views and tables.
* **Grain:** One row per `product_id`.

## Modeling Decisions (Rationale)
* **Aggregation:** Performed in BigQuery, not Looker Studio, to ensure accuracy and performance.
* **Semantic Views:** Explicit, not implied, to avoid confusion and drift.
* **Mapping:** Each dashboard visual maps cleanly to a single source, preventing metric inconsistency.
