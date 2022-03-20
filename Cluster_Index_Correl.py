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


SPI_df = pd.DataFrame(index = center_SPI12.drop("Ano", axis = 1, inplace = False).columns, columns = clim_index.drop(["Ano", "Mes"], axis = 1, inplace = False).columns)
b1_df = pd.DataFrame(index = center_b1.drop("Ano", axis = 1, inplace = False).columns, columns = clim_index.drop(["Ano", "Mes"], axis = 1, inplace = False).columns)
b2_df = pd.DataFrame(index = center_b2.drop("Ano", axis = 1, inplace = False).columns, columns = clim_index.drop(["Ano", "Mes"], axis = 1, inplace = False).columns)
b3_df = pd.DataFrame(index = center_b3.drop("Ano", axis = 1, inplace = False).columns, columns = clim_index.drop(["Ano", "Mes"], axis = 1, inplace = False).columns)

#%%
for i in center_SPI12.drop("Ano", axis = 1, inplace = False).columns:
    for j in index_mean.drop("Ano", axis = 1, inplace = False):
        SPI_df.loc[i, j] = spearmanr(center_SPI12[i], index_mean[j])[0]

for i in center_b1.drop("Ano", axis = 1, inplace = False):
    for j in index_mean.drop("Ano", axis = 1, inplace = False):
        b1_df.loc[i, j] = spearmanr(center_b1[i], index_mean[j])[0]

for i in center_b2.drop("Ano", axis = 1, inplace = False):
    for j in index_mean.drop("Ano", axis = 1, inplace = False):
        b2_df.loc[i, j] = spearmanr(center_b2[i], index_mean[j])[0]

for i in center_b3.drop("Ano", axis = 1, inplace = False):
    for j in index_mean.drop("Ano", axis = 1, inplace = False):
        b3_df.loc[i, j] = spearmanr(center_b3[i], index_mean[j])[0]

# %%
SPI_df = SPI_df.astype("float64")
b1_df = b1_df.astype("float64")
b2_df = b2_df.astype("float64")
b3_df = b3_df.astype("float64")

#%%
fig, ax = plt.subplots(dpi = 600)
sns.heatmap(SPI_df, ax = ax, cmap = "seismic_r", linewidths = 1,
            linecolor = "white",
            cbar_kws = {"label":"Spearman Correlation (\u03C1)"},
            annot = True, fmt = ".2f")
ax.set_title("SPI12-Dez (1950-2016)")
fig.savefig("{}/Figuras/SPI12_M_Corr_P.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

#%%
fig1, ax1 = plt.subplots(dpi = 600)
sns.heatmap(b1_df, ax = ax1, cmap = "seismic_r", linewidths = 1,
            linecolor = "white",
            cbar_kws = {"label":"Spearman Correlation (\u03C1)"},
            annot = True, fmt = ".2f")
ax1.set_title("Banda de Alta Frequência: 2 até 8 anos (1951-2016)")
fig1.savefig("{}/Figuras/Band1_M_Corr_P.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

#%%
fig2, ax2 = plt.subplots(dpi = 600)
sns.heatmap(b2_df, ax = ax2, cmap = "seismic_r", linewidths = 1,
            linecolor = "white",
            cbar_kws = {"label":"Spearman Correlation (\u03C1)"},
            annot = True, fmt = ".2f")
ax2.set_title("Banda de Média Frequência: 9 até 40 anos (1951-2016)")
fig2.savefig("{}/Figuras/Band2_M_Corr_P.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

#%%
fig3, ax3 = plt.subplots(dpi = 600)
sns.heatmap(b3_df, ax = ax3, cmap = "seismic_r", linewidths = 1,
            linecolor = "white",
            cbar_kws = {"label":"Spearman Correlation (\u03C1)"},
            annot = True, fmt = ".2f")
ax3.set_title("Banda de Baixa Frequência: 40+ anos (1951-2016)")
fig3.savefig("{}/Figuras/Band3_M_Corr_P.png".format(os.getcwd()), dpi = 600, bbox_inches = "tight", facecolor = "w")

# %%

# %%
