def load_data(df):

    output_path = "data/processed/cleaned_customers.csv"

    df.to_csv(output_path, index=False)

    print("Data Loaded Successfully")
    print("Saved to:", output_path)