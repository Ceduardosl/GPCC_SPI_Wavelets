#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import seaborn as sns
#%%

center_SPI12 = pd.read_csv("{}/Dados/SPI12_Center.csv".format(os.getcwd()), sep = ";")

center_b1 = pd.read_csv("{}/Dados/Band1_Center.csv".format(os.getcwd()), sep = ";")

center_b2 = pd.read_csv("{}/Dados/Band2_Center.csv".format(os.getcwd()), sep = ";")

center_b3 = pd.read_csv("{}/Dados/Band3_Center.csv".format(os.getcwd()), sep = ";")

clim_index = pd.read_csv("{}/Dados/Climate_Indices.csv".format(os.getcwd()), sep = ";")
clim_index = clim_index.loc[(clim_index["Ano"] >= 1950) & (clim_index["Ano"] <= 2016)]
index_mean = clim_index.groupby("Ano", as_index = False).mean()
index_mean.drop("Mes", axis = 1, inplace = True)

# %%
fig, ax = plt.subplots(8,5,dpi = 600, figsize=(20, 20), sharex = True)

for i in range(0,4+1,1):
    ax[0,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 1"], c = "green", label = "Cluster 1")
    ax[0,i].legend()
for i in range(0,4+1,1):
    ax[1,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 2"], c = "red",  label = "Cluster 2")
    ax[1,i].legend()
for i in range(0,4+1,1):
    ax[2,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 3"], c = "blue",  label = "Cluster 3")
    ax[2,i].legend()
for i in range(0,4+1,1):
    ax[3,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 4"], c = "darkorange",  label = "Cluster 4")
    ax[3,i].legend()
for i in range(0,4+1,1):
    ax[4,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 5"], c = "black",  label = "Cluster 5")
    ax[4,i].legend()
for i in range(0,4+1,1):
    ax[5,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 6"], c = "darkmagenta",  label = "Cluster 6")
    ax[5,i].legend()
for i in range(0,4+1,1):
    ax[6,i].plot(center_SPI12["Ano"], center_SPI12["Cluster 7"], c = "darkcyan", label = "Cluster 7")
    ax[6,i].legend()

ax[7,0].bar(index_mean["Ano"], index_mean["Nino"], label = "Nino 3.4")
ax[7,0].axhline(y = 0, c = "black", lw = 0.5)
ax[7,0].legend()
ax[7,1].bar(index_mean["Ano"], index_mean["PDO"], label = "PDO")
ax[7,1].axhline(y = 0, c = "black", lw = 0.5)
ax[7,1].legend()
ax[7,2].bar(index_mean["Ano"], index_mean["AMO"], label = "AMO")
ax[7,2].axhline(y = 0, c = "black", lw = 0.5)
ax[7,2].legend()
ax[7,3].bar(index_mean["Ano"], index_mean["TNA"], label = "TNA")
ax[7,3].axhline(y = 0, c = "black", lw = 0.5)
ax[7,3].legend()
ax[7,4].bar(index_mean["Ano"], index_mean["TSA"], label = "TSA")
ax[7,4].axhline(y = 0, c = "black", lw = 0.5)
ax[7,4].legend()
ax[0,2].set_title("SPI12 (1951 - 2016)", fontsize = 20)

fig.savefig("{}/Figuras/SPI12.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

# %%
fig, ax = plt.subplots(8,5,dpi = 600, figsize=(20, 20), sharex = True)

for i in range(0,4+1,1):
    ax[0,i].plot(center_b1["Ano"],center_b1["Cluster 1"], c = "green", label = "Cluster 1")
    ax[0,i].legend()
for i in range(0,4+1,1):
    ax[1,i].plot(center_b1["Ano"],center_b1["Cluster 2"], c = "red",  label = "Cluster 2")
    ax[1,i].legend()
for i in range(0,4+1,1):
    ax[2,i].plot(center_b1["Ano"],center_b1["Cluster 3"], c = "blue",  label = "Cluster 3")
    ax[2,i].legend()
for i in range(0,4+1,1):
    ax[3,i].plot(center_b1["Ano"],center_b1["Cluster 4"], c = "darkorange",  label = "Cluster 4")
    ax[3,i].legend()
for i in range(0,4+1,1):
    ax[4,i].plot(center_b1["Ano"],center_b1["Cluster 5"], c = "black",  label = "Cluster 5")
    ax[4,i].legend()
for i in range(0,4+1,1):
    ax[5,i].plot(center_b1["Ano"],center_b1["Cluster 6"], c = "darkmagenta",  label = "Cluster 6")
    ax[5,i].legend()
for i in range(0,4+1,1):
    ax[6,i].plot(center_b1["Ano"],center_b1["Cluster 7"], c = "darkcyan", label = "Cluster 7")
    ax[6,i].legend()

ax[7,0].bar(index_mean["Ano"], index_mean["Nino"], label = "Nino 3.4")
ax[7,0].axhline(y = 0, c = "black", lw = 0.5)
ax[7,0].legend()
ax[7,1].bar(index_mean["Ano"], index_mean["PDO"], label = "PDO")
ax[7,1].axhline(y = 0, c = "black", lw = 0.5)
ax[7,1].legend()
ax[7,2].bar(index_mean["Ano"], index_mean["AMO"], label = "AMO")
ax[7,2].axhline(y = 0, c = "black", lw = 0.5)
ax[7,2].legend()
ax[7,3].bar(index_mean["Ano"], index_mean["TNA"], label = "TNA")
ax[7,3].axhline(y = 0, c = "black", lw = 0.5)
ax[7,3].legend()
ax[7,4].bar(index_mean["Ano"], index_mean["TSA"], label = "TSA")
ax[7,4].axhline(y = 0, c = "black", lw = 0.5)
ax[7,4].legend()
ax[0,2].set_title("Banda 1 -> 2 até 9 anos (1951 - 2016)", fontsize = 20)

fig.savefig("{}/Figuras/Band1.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

# %%
fig, ax = plt.subplots(6,5,dpi = 600, figsize=(20, 20), sharex = True)

for i in range(0,4+1,1):
    ax[0,i].plot(center_b2["Ano"],center_b2["Cluster 1"], c = "green", label = "Cluster 1")
    ax[0,i].legend()
for i in range(0,4+1,1):
    ax[1,i].plot(center_b2["Ano"],center_b2["Cluster 2"], c = "red",  label = "Cluster 2")
    ax[1,i].legend()
for i in range(0,4+1,1):
    ax[2,i].plot(center_b2["Ano"],center_b2["Cluster 3"], c = "blue",  label = "Cluster 3")
    ax[2,i].legend()
for i in range(0,4+1,1):
    ax[3,i].plot(center_b2["Ano"],center_b2["Cluster 4"], c = "darkorange",  label = "Cluster 4")
    ax[3,i].legend()
for i in range(0,4+1,1):
    ax[4,i].plot(center_b2["Ano"],center_b2["Cluster 5"], c = "black",  label = "Cluster 5")
    ax[4,i].legend()


ax[5,0].bar(index_mean["Ano"], index_mean["Nino"], label = "Nino 3.4")
ax[5,0].axhline(y = 0, c = "black", lw = 0.5)
ax[5,0].legend()
ax[5,1].bar(index_mean["Ano"], index_mean["PDO"], label = "PDO")
ax[5,1].axhline(y = 0, c = "black", lw = 0.5)
ax[5,1].legend()
ax[5,2].bar(index_mean["Ano"], index_mean["AMO"], label = "AMO")
ax[5,2].axhline(y = 0, c = "black", lw = 0.5)
ax[5,2].legend()
ax[5,3].bar(index_mean["Ano"], index_mean["TNA"], label = "TNA")
ax[5,3].axhline(y = 0, c = "black", lw = 0.5)
ax[5,3].legend()
ax[5,4].bar(index_mean["Ano"], index_mean["TSA"], label = "TSA")
ax[5,4].axhline(y = 0, c = "black", lw = 0.5)
ax[5,4].legend()
ax[0,2].set_title("Banda 2 -> 9 até 40 anos (1951 - 2016)", fontsize = 20)

fig.savefig("{}/Figuras/Band2.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

# %%
fig, ax = plt.subplots(4,5,dpi = 600, figsize=(20, 20), sharex = True)

for i in range(0,4+1,1):
    ax[0,i].plot(center_b3["Ano"],center_b3["Cluster 1"], c = "green", label = "Cluster 1")
    ax[0,i].legend()
for i in range(0,4+1,1):
    ax[1,i].plot(center_b3["Ano"],center_b3["Cluster 2"], c = "red",  label = "Cluster 2")
    ax[1,i].legend()
for i in range(0,4+1,1):
    ax[2,i].plot(center_b3["Ano"],center_b3["Cluster 3"], c = "blue",  label = "Cluster 3")
    ax[2,i].legend()

ax[3,0].bar(index_mean["Ano"], index_mean["Nino"], label = "Nino 3.4")
ax[3,0].axhline(y = 0, c = "black", lw = 0.5)
ax[3,0].legend()
ax[3,1].bar(index_mean["Ano"], index_mean["PDO"], label = "PDO")
ax[3,1].axhline(y = 0, c = "black", lw = 0.5)
ax[3,1].legend()
ax[3,2].bar(index_mean["Ano"], index_mean["AMO"], label = "AMO")
ax[3,2].axhline(y = 0, c = "black", lw = 0.5)
ax[3,2].legend()
ax[3,3].bar(index_mean["Ano"], index_mean["TNA"], label = "TNA")
ax[3,3].axhline(y = 0, c = "black", lw = 0.5)
ax[3,3].legend()
ax[3,4].bar(index_mean["Ano"], index_mean["TSA"], label = "TSA")
ax[3,4].axhline(y = 0, c = "black", lw = 0.5)
ax[3,4].legend()
ax[0,2].set_title("Banda 3 -> 40+ anos (1951 - 2016)", fontsize = 20)

fig.savefig("{}/Figuras/Band3.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

# %%
