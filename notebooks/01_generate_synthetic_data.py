
#INSTALL PACKAGES
!pip install pandas numpy faker


import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()
np.random.seed(42)

N_PRODUCTS = 50
N_DAYS = 365

products = pd.DataFrame({
    "product_id": range(1, N_PRODUCTS + 1),
    "product_family": np.random.choice(
        ["CPU", "GPU", "AI_Accelerator"], N_PRODUCTS
    ),
    "architecture": np.random.choice(
        ["Zen4", "Zen5", "CDNA3"], N_PRODUCTS
    )
})

dates = pd.date_range("2024-01-01", periods=N_DAYS)

records = []
for _, row in products.iterrows():
    base_yield = np.random.uniform(0.85, 0.98)
    for date in dates:
        records.append({
            "date": date,
            "product_id": row.product_id,
            "yield_pct": min(
                1.0, max(0.5, np.random.normal(base_yield, 0.03))
            ),
            "defect_rate": np.random.uniform(0.01, 0.08),
            "units_produced": int(np.random.normal(5000, 800)),
            "avg_latency_ms": np.random.uniform(10, 40),
            "throughput_ops": np.random.uniform(1e6, 1e7),
            "forecast_demand": int(np.random.normal(4800, 700)),
            "actual_demand": int(np.random.normal(5000, 900)),
            "revenue_usd": np.random.uniform(1e6, 8e6)
        })

fact_metrics = pd.DataFrame(records)

# Validation checks
assert fact_metrics["yield_pct"].between(0,1).all()
assert fact_metrics["units_produced"].min() > 0

fact_metrics.head()


fact_metrics.to_csv('fact_metrics.csv', index=False)
print('Data saved to fact_metrics.csv')
