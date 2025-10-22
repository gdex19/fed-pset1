import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_one_country(df, country, col, gdp_type, title):
    df_country = df.query("country == @country")
    if len(gdp_type) == 1:
        df_plot = df_country.query("gdp_type == @gdp_type")
        ax = sns.lineplot(data=df_plot, x="year", y=col)
    elif len(gdp_type)== 2:
        ax = sns.lineplot(data=df_country, x="year", y=col, hue="gdp_type")
    else:
        return None
    ax.xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.title(title)
    
def plot_all_countries(df, col, gdp_type, title):
    df_plot = df.query("gdp_type == @gdp_type")
    ax = sns.lineplot(data=df_plot, x="year", y=col, hue="country")
    ax.xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.title(title)   