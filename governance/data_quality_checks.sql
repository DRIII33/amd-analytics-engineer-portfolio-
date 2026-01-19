-- Check 1: Ensure no null product IDs
SELECT COUNT(*) AS null_product_ids
FROM `driiiportfolio.raw.fact_product_metrics`
WHERE product_id IS NULL;

-- Check 2: Validate yield percentage range
SELECT COUNT(*) AS invalid_yield_values
FROM `driiiportfolio.raw.fact_product_metrics`
WHERE yield_pct < 0 OR yield_pct > 1;

-- Check 3: Validate defect rate range
SELECT COUNT(*) AS invalid_defect_rates
FROM `driiiportfolio.raw.fact_product_metrics`
WHERE defect_rate < 0 OR defect_rate > 1;

-- Check 4: Ensure non-negative units produced
SELECT COUNT(*) AS negative_units
FROM `driiiportfolio.raw.fact_product_metrics`
WHERE units_produced < 0;

-- Check 5: Detect missing daily metrics
SELECT date, COUNT(*) AS missing_records
FROM `driiiportfolio.raw.fact_product_metrics`
GROUP BY date
HAVING COUNT(*) = 0;
