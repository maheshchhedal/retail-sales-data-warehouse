import sys
import os
import pandas as pd

# Add the extract folder to Python's path so we can import load_raw directly
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'extract'))
from load_raw import load_raw_data


def explore_data(df):
    # Basic checks to understand the raw data before cleaning
    print("Shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


# from elt.extract.load_raw import load_raw_data

# def explore_data(df):
#     print("Shape:", df.shape)
#     print("\nData types:\n", df.dtypes)
#     print("\nMissing values:\n", df.isnull().sum())
#     print("\nDuplicate rows:", df.duplicated().sum())


def clean_data(df):
    # Standardize column names: lowercase, no spaces, no extra whitespace
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Convert date columns from text to actual datetime type
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])

    return df  # return the cleaned dataframe so it can be used outside this function


if __name__ == "__main__":
    df = load_raw_data()          # load raw data
    explore_data(df)               # check it before cleaning
    df = clean_data(df)            # clean it, and save the cleaned version
    print(df.dtypes)                # confirm order_date/ship_date are now datetime64