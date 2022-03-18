#%%
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#%%
spi12 = pd.read_csv("{}/Dados/SPI12-Dez.csv".format(os.getcwd()), sep = ";", header = None)
band1 = pd.read_csv("{}/Dados/band1.csv".format(os.getcwd()), sep = ";", header = None)
band2 = pd.read_csv("{}/Dados/band2.csv".format(os.getcwd()), sep = ";", header = None)
band3 = pd.read_csv("{}/Dados/band3.csv".format(os.getcwd()), sep = ";", header = None)

#%%
if (spi12.iloc[:2,].equals(band1.iloc[:2,])) & (band1.iloc[:2,].equals(band2.iloc[:2,])) & (band2.iloc[:2,].equals(band3.iloc[:2,])) :
    coords = spi12.iloc[:2,]
else:
    print("Coordenadas divergem entre os dataframes")

spi_df = spi12.iloc[2:,]
b1_df = band1.iloc[2:,]
b2_df = band2.iloc[2:,]
b3_df = band3.iloc[2:,]

# %%
