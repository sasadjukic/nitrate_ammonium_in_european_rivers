
import pandas as pd 
import matplotlib.pyplot as plt 
from data import ammonium_17

# sort dataframe from lower to higher
sort_ammonium_17 = ammonium_17.sort_values(['values'], ascending=True)

# get country and values from sorted dataframe
country = [country for country in sort_ammonium_17['country']]
values = [value for value in sort_ammonium_17['values']]
color = '#387668'

fig, ax = plt.subplots()

# create horizontal bar
plt.barh(
    country,
    values,
    color=color
)

# delete box edges
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# display values
for index, value in enumerate(values):
        plt.text(
            value, 
            index,
            str(value),
            ha = 'center',
            position = (value+7, index-0.2),
            fontsize = 12.5,
            color = color
        )

plt.show()
