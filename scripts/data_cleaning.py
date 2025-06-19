#%%
import pandas as pd
import os 
#%%
path = "/Users/jayco/Library/Mobile Documents/com~apple~CloudDocs/Projects/MSThesis/Data/Project_Data"
os.chdir(path)
#%%
dfs = {}

for filename in os.listdir(path):
    if filename.endswith(".csv"):
        key = filename.replace(".csv", "").replace("-", "_")
        full_path = os.path.join(path, filename)
        df = pd.read_csv(full_path)
        dfs[key] = df

for key in dfs:
    df = dfs[key]
    if 'Year' in df.columns:
        dfs[key] = df[df['Year'] >= 1935].copy()
    globals()[key] = dfs[key].copy()

#%%
from functools import reduce

for df in [usgs_cobalt_data, usgs_graphite_data, usgs_lithium_data, usgs_manganese_data, usgs_nickel_data]:
    df.columns = df.columns.str.strip()

usgs_cobalt_data = usgs_cobalt_data[['Year', 'Unit value ($/t)', 'World mine production']]
usgs_graphite_data = usgs_graphite_data[['Year', 'Unit value ($/t)', 'World production']]
usgs_lithium_data = usgs_lithium_data[['Year', 'Unit value ($/t)', 'World production (lithium content)']]
usgs_manganese_data = usgs_manganese_data[['Year', 'Unit value ($/t)', 'World production']]
usgs_nickel_data = usgs_nickel_data[['Year', 'Unit value  ($/t)', 'World production']]

metal_dfs = {
    'cobalt': usgs_cobalt_data,
    'graphite': usgs_graphite_data,
    'lithium': usgs_lithium_data,
    'manganese': usgs_manganese_data,
    'nickel': usgs_nickel_data,
}

for metal, df in metal_dfs.items():
    clean_cols = []
    for col in df.columns:
        if col == 'Year':
            clean_cols.append('Year')
        else:
            col_clean = col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace("$", "usd")
            clean_cols.append(f"{metal}_{col_clean}")
    df.columns = clean_cols
    metal_dfs[metal] = df

combined_metal_df = reduce(
    lambda left, right: pd.merge(left, right, on='Year', how='outer'),
    metal_dfs.values()
)

combined_metal_df.head()

#%%
gdp_cpi = pd.merge(bea_real_gdp, BLS_CPI_vehicle)

gdp_cpi.rename(columns={'GDP (billions of chained 2017 USD)' : 'gdp_billions_of_chained_2017', 'GDP (billions USD)' : 'gdp_billions_usd', 'Annual' : 'new_vehicle_cpi_index_1982-1984'}, inplace=True)

gdp_cpi

#%%
final_df = pd.merge(combined_metal_df, gdp_cpi)

final_df.head()

final_df.to_csv(path+'/final_project_data.csv', index=False)