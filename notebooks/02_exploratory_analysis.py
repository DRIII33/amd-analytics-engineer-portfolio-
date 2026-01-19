#INSTALL PACKAGES
!pip install pandas numpy matplotlib


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.float_format", "{:,.4f}".format)

df = pd.read_csv("fact_product_metrics.csv")

df.head()

# Row count & schema validation
# assert df.shape[0] > 100_000, "Unexpected row volume"
assert df["yield_pct"].between(0, 1).all()

# Null inspection
df.isnull().mean().sort_values(ascending=False)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

df["yield_pct"].hist(ax=ax[0], bins=40)
ax[0].set_title("Yield Distribution")

df["defect_rate"].hist(ax=ax[1], bins=40)
ax[1].set_title("Defect Rate Distribution")

metrics = [
    "yield_pct",
    "defect_rate",
    "avg_latency_ms",
    "throughput_ops",
    "revenue_usd"
]

corr = df[metrics].corr()

corr

daily = (
    df.groupby("date")
    .agg(
        avg_yield=("yield_pct", "mean"),
        avg_revenue=("revenue_usd", "mean")
    )
)

daily.plot(figsize=(12, 5), title="Daily Yield vs Revenue Trend")

df["demand_accuracy"] = df["actual_demand"] / df["forecast_demand"]

df["demand_accuracy"].describe()

high_defect = df[df["defect_rate"] > 0.15]

high_defect[["product_id", "defect_rate"]].head()

summary = {
    "rows": df.shape[0],
    "products": df["product_id"].nunique(),
    "avg_yield": df["demand_accuracy"].mean(),
    "avg_demand_accuracy": df["demand_accuracy"].mean()
}

summary
