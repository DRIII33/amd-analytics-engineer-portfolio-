CREATE OR REPLACE TABLE `driiiportfolio.raw.fact_product_metrics` (
  date DATE,
  product_id INT64,
  yield_pct FLOAT64,
  defect_rate FLOAT64,
  units_produced INT64,
  avg_latency_ms FLOAT64,
  throughput_ops FLOAT64,
  forecast_demand INT64,
  actual_demand INT64,
  revenue_usd FLOAT64
);

