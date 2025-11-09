import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def plot_one_country(
    df: pd.DataFrame, country: str, col: str, gdp_type: str, title: str
) -> None:
    df_country = df[df["country"] == country]
    if len(gdp_type) == 1:
        df_plot = df_country[df_country["gdp_type"] == gdp_type]
        ax = sns.lineplot(data=df_plot, x="year", y=col)
    elif len(gdp_type) == 2:
        ax = sns.lineplot(data=df_country, x="year", y=col, hue="gdp_type")
    else:
        return None
    ax.xaxis.set_major_locator(MaxNLocator(8))
    plt.title(title)


def plot_all_countries(
    df: pd.DataFrame, col: str, gdp_type: str, title: str
) -> None:
    df_plot = df[df["gdp_type"] == gdp_type]
    ax = sns.lineplot(data=df_plot, x="year", y=col, hue="country")
    ax.xaxis.set_major_locator(MaxNLocator(8))
    plt.title(title)
