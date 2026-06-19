def clean_data(df):

    print("Before Cleaning:")
    print(df)

    df = df.dropna()

    df["age"] = df["age"].astype(int)

    print("After Cleaning:")
    print(df)

    return df