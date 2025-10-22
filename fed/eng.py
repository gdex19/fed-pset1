import pandas as pd

def select_columns(df):
    cols_to_keep = ["country"] + [str(i) for i in range(2000, 2023)]
    return df[cols_to_keep].copy()

def select_countries(df, countries):
   mask = df["country"].isin(countries)
   return df[mask].copy()
   
def wide_to_long(df):
    df_long = pd.melt(df, id_vars=["country"], var_name="year",
                      value_vars=[str(i) for i in range(2000, 2023)],
                      value_name="gdp")
    return df_long

def clean_data(df, countries):
    df = select_columns(df)
    df = select_countries(df, countries)
    df_long = wide_to_long(df)
    return df_long

def add_percent_change(df_long):
    df_long = df_long.sort_values(by=["country", "year"], ascending=True)
    df_long["pct_chg"] = df_long.groupby(by=["country"])["gdp"].pct_change() * 100
    return df_long

def normalize_to_2000(df_long):
    df_long = df_long.sort_values(by=["country", "year"], ascending=True)
    df_long["normed_gdp"] = df_long.groupby("country", group_keys=False)["gdp"].apply(
        lambda x: x / x.iloc[0] * 100
    )
    return df_long

def add_features(df_long):
    df_pct = add_percent_change(df_long)
    df_normalized = normalize_to_2000(df_pct)
    return df_normalized



def combine_dfs(df_usd, df_ppp):
    df_combined = pd.concat([df_usd.assign(gdp_type="usd"), df_ppp.assign(gdp_type="ppp")],
                            ignore_index=True
    )
    return df_combined