CREATE OR REPLACE VIEW `driiiportfolio.raw.stg_product_metrics` AS
SELECT
  date,
  product_id,
  SAFE_DIVIDE(actual_demand, forecast_demand) AS demand_accuracy,
  yield_pct,
  defect_rate,
  units_produced,
  avg_latency_ms,
  throughput_ops,
  revenue_usd
FROM `driiiportfolio.raw.fact_product_metrics`
WHERE yield_pct IS NOT NULL;
