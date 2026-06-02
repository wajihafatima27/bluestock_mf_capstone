import requests
import pandas as pd
import os

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_folder = "data/raw"

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{fund_name}_live_nav.csv"

        nav_df.to_csv(
            os.path.join(output_folder, file_name),
            index=False
        )

        print(f"Saved: {file_name}")

    else:
        print(f"Failed: {fund_name}")