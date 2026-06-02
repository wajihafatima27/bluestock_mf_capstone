import pandas as pd
import os

DATA_PATH = "data/raw"

print("=" * 60)
print("DATA INGESTION STARTED")
print("=" * 60)

for file in os.listdir(DATA_PATH):

    if file.endswith(".csv"):

        file_path = os.path.join(DATA_PATH, file)

        print("\n" + "=" * 60)
        print(f"Dataset: {file}")
        print("=" * 60)

        try:
            df = pd.read_csv(file_path)

            print("Shape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

        except Exception as e:
            print(f"Error reading {file}: {e}")

print("\nData ingestion completed successfully.")