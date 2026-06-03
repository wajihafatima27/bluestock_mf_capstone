import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(df.dtypes)

print("\nExpense Ratio Summary")
print(df["expense_ratio_pct"].describe())

print("\nRisk Grades")
print(df["risk_grade"].value_counts())

print("\nMorningstar Ratings")
print(df["morningstar_rating"].value_counts())