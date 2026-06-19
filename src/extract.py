import pandas as pd

def extract_data():

    df = pd.read_csv(
        "data/raw/customers.csv"
    )

    print("Data Extracted")

    return df