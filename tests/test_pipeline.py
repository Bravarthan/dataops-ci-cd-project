from src.extract import extract_data
from src.transform import clean_data

def test_extract_data():

    df = extract_data()

    assert df is not None
    assert len(df) > 0


def test_transform_data():

    df = extract_data()
    clean_df = clean_data(df)

    assert clean_df.isnull().sum().sum() == 0