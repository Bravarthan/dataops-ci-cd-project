from extract import extract_data
from transform import clean_data
from load import load_data

def run_pipeline():

    df = extract_data()

    clean_df = clean_data(df)

    load_data(clean_df)

if __name__ == "__main__":
    run_pipeline()