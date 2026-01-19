CREATE OR REPLACE VIEW `driiiportfolio.raw.product_performance_summary` AS
SELECT
  product_id,
  COUNT(DISTINCT date) AS active_days,
  AVG(yield_pct) AS avg_yield,
  AVG(defect_rate) AS avg_defect_rate,
  AVG(demand_accuracy) AS avg_demand_accuracy,
  AVG(avg_latency_ms) AS avg_latency_ms,
  SUM(units_produced) AS total_units,
  SUM(revenue_usd) AS total_revenue
FROM `driiiportfolio.raw.stg_product_metrics`
GROUP BY product_id;
