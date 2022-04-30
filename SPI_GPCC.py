#%%
import os
import pandas as pd
from standard_precip.spi import SPI
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
#%%
dir_shp = "{}/Shapes/BR_UF_2020.shp".format(os.getcwd())
dir_dados = "{}/Dados/Pr_GPCC_Brasil.csv".format(os.getcwd())

GPCC = pd.read_csv(dir_dados, sep = ";").T
shp = gpd.read_file(dir_shp)
#%%
pr_df = GPCC.iloc[2:,]
pr_df.index = pd.date_range(start = "1891-01-01", end = "2016-12-31", freq = "M", inclusive = "both")
coords = GPCC.iloc[[0,1],:]

coords.insert(0, "Coords", coords.index)
coords.reset_index(inplace = True, drop = True)

pr = pr_df.loc[pr_df.index.year >= 1950]
pr.insert(0, "Date", pr.index)
pr.reset_index(inplace = True, drop = True)
pr.columns = pr.columns.astype(str)


spi_fun = SPI()
spi12 = spi_fun.calculate(pr, "Date", pr.columns[1:], freq = "M",
                        scale = 12, fit_type="lmom", dist_type="gam")

for i in spi12.columns[1:]:
    if i.split("_")[-1] != "index":
        spi12.drop(i, axis = 1, inplace = True)

coords.columns = spi12.columns
spiDez = pd.concat([coords, spi12.loc[spi12["Date"].dt.month == 12]])
spiDez.to_csv("{}/Dados/SPI12-Dez.csv".format(os.getcwd()), sep = ";", index = None, header = False)
#%%

fig, ax = plt.subplots()
for i in spiDez.columns[1:]:
    ax.plot(spiDez["Date"], spiDez[i], alpha = 0.5, lw = 0.5)
# %%
