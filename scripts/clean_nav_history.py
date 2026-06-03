import pandas as pd

print("Loading NAV history...")

df = pd.read_csv("data/raw/02_nav_history.csv")

# Parse dates
df["date"] = pd.to_datetime(df["date"])

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print(f"Duplicates removed: {before - after}")

# Remove invalid NAV values
df = df[df["nav"] > 0]

all_funds = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    full_dates = pd.date_range(
        start=group["date"].min(),
        end=group["date"].max(),
        freq="D"
    )

    group = (
        group
        .set_index("date")
        .reindex(full_dates)
    )

    group["amfi_code"] = amfi_code

    # Weekend/Holiday handling
    group["nav"] = group["nav"].ffill()

    group = group.reset_index()

    group.rename(
        columns={"index": "date"},
        inplace=True
    )

    all_funds.append(group)

clean_df = pd.concat(all_funds)

clean_df = clean_df[
    ["amfi_code", "date", "nav"]
]

clean_df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("\nFinal Shape:")
print(clean_df.shape)

print("\nNAV cleaning completed successfully.")