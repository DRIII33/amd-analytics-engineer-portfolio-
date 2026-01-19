CREATE OR REPLACE VIEW raw.product_performance_summary AS
SELECT
  product_id,
  COUNT(DISTINCT date) AS active_days,
  AVG(yield_pct) AS avg_yield,
  AVG(defect_rate) AS avg_defect_rate,
  AVG(actual_demand / NULLIF(forecast_demand,0)) AS avg_demand_accuracy,
  AVG(avg_latency_ms) AS avg_latency_ms,
  SUM(units_produced) AS total_units,
  SUM(revenue_usd) AS total_revenue
FROM raw.stg_product_metrics
GROUP BY product_id;
