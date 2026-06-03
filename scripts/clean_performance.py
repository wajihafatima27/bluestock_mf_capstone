import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

# Numeric validation
for col in returns_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Expense ratio anomaly check
expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense Ratio Anomalies:",
    len(expense_anomalies)
)

# Missing values check
print(
    "Missing Values:",
    df.isnull().sum().sum()
)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Final Shape:", df.shape)
print("Performance cleaning completed.")