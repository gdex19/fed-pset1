import pandas as pd


def load_data(fp: str) -> pd.DataFrame:
    df = pd.read_csv(fp, skiprows=3)
    country_col = "Country Name"
    df = df.rename(columns={country_col: "country"})
    return df
