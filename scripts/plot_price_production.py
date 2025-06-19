# %%
import matplotlib.pyplot as plt
import pandas as pd

# %%
data = pd.read_csv(
    '/Users/jayco/Library/Mobile Documents/com~apple~CloudDocs/Projects/MSThesis/Data/Project_Data/final_project_data.csv')
filtered = data[data.columns[0:11]]

#%%
metals = {
    'cobalt': {
        'price': 'cobalt_unit_value_usd_t',
        'production': 'cobalt_world_mine_production'
    },
    'graphite': {
        'price': 'graphite_unit_value_usd_t',
        'production': 'graphite_world_production'
    },
    'lithium': {
        'price': 'lithium_unit_value_usd_t',
        'production': 'lithium_world_production_lithium_content'
    },
    'nickel': {
        'price': 'nickel_unit_value__usd_t',
        'production': 'nickel_world_production'
    },
    'manganese': {
        'price': 'manganese_unit_value_usd_t',
        'production': 'manganese_world_production'
    }
}

fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 14), sharex=True)
axes.flatten()
for ax, (metal, cols) in zip(axes, metals.items()):
    # Left y-axis: price
    ax.plot(filtered['Year'], filtered[cols['price']],
            label='Price', color='lightblue')
    ax.set_title(metal.capitalize())
    ax.set_xlabel('Year')
    ax.set_ylabel('Unit Value (USD/t)')

    # Right y-axis: production
    ax2 = ax.twinx()
    ax2.plot(filtered['Year'], filtered[cols['production']],
             label='Production', color='orange')
    ax2.set_ylabel('World Production (tons)')

    ax.legend(loc='upper left')
    ax2.legend(loc='upper left')

# Tidy up spacing
plt.tight_layout()
plt.show()

#%%
fig.savefig('/Users/jayco/Library/Mobile Documents/com~apple~CloudDocs/Projects/MSThesis/images/price_production.png')