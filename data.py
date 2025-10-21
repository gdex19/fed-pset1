import pandas as pd

# Load CSV file (from GitHub or local)
url = "https://raw.githubusercontent.com/username/repo/main/data.csv"  # replace with your actual URL
df = pd.read_csv(url)

# Select the countries you want
countries = ['USA', 'Canada', 'Japan']
df = df[df['Country'].isin(countries)]

# Convert wide format to long format
df_long = df.melt(id_vars='Country', var_name='Year', value_name='GDP')

# Convert Year to numeric and filter 2000–2022
df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')
df_long = df_long[df_long['Year'].between(2000, 2022)]

# Check the result
print(df_long.head())

# (Optional) Save to new CSV
df_long.to_csv("gdp_selected_countries.csv", index=False)
