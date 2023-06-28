
import pandas as pd 

# read excel data
nitrate = pd.read_excel('nitrate_in_rivers_Europe.xlsx')
ammonium = pd.read_excel('ammonium_in_rivers_Europe.xlsx')

# drop rows before 2000 (some data repeats in those rows anyway)
nitrate_00_17 = nitrate.drop(nitrate[nitrate['time_period'] == '1992-2017'].index)
ammonium_00_17 = ammonium.drop(ammonium[ammonium.time_period == '1992-2017'].index)

# select the latest data (2017)
nitrate_17 = nitrate_00_17[nitrate_00_17['year'] == 2017]
ammonium_17 = ammonium_00_17[ammonium_00_17['year'] == 2017]