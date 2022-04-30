#%%
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import os

#%%
def rename_columns(df):
    col_list = []
    for i in df.columns:
        col_list.append("Cluster {}".format(int(i) + 1))

    df.columns = col_list
    return(df)

def spatial_plot(df, shp, dict_scatter, title, fig_name):

    os.makedirs("{}/Figuras".format(os.getcwd()), exist_ok = True)
    dict_plot = [] #Para Coletar apenas as legendas das classes utilizadas
    
    for j in dict_scatter:
        if j["Class"] in np.arange(df["Class"].min(), df["Class"].max()+1):
            dict_plot.append(j)
    
    fig, ax = plt.subplots(figsize = (6,6), dpi = 600)
    for i in dict_plot:
        ax.scatter(
            x = df["lon"].loc[df["Class"] == i["Class"]], 
            y = df["lat"].loc[df["Class"] == i["Class"]],
            c = i["color"], label = i["label"], s = 10, zorder = 3)

    shp.plot(
        ax = ax,  color = "None", linestyle = "solid",
        alpha = 1, linewidth=0.5, zorder = 2)

    ax.grid(linestyle = "--", alpha = 0.5, zorder = 1)

    ax.legend(
        loc = "lower right", markerfirst = True, handletextpad = 0.1,
        borderaxespad = 0.3, fontsize = 10,  markerscale = 1.5)

    ax.set_ylabel("Latitude")
    ax.set_xlabel("Longitude")
    ax.set_title(title, loc = "left")

    fig.savefig(
        "{}/Figuras/{}.png".format(os.getcwd(), fig_name),
        dpi = 600, bbox_inches = "tight", facecolor = "w")
    
    plt.close()

def center_plot(df, dict_scatter, title, fig_name, ylim):

    os.makedirs("{}/Figuras".format(os.getcwd()), exist_ok = True)
    for i in df.columns[1:]:
        fig, ax = plt.subplots(dpi = 600)
        for j in dict_scatter:
            if i == "Cluster {}".format(j["Class"] + 1):
                ax.plot(
                    df["Ano"], df[i],
                    marker = "o", c = j["color"])
                ax.grid(linestyle='--', c = "black", alpha = 0.4)
                ax.axhline(y = 0, c = "black", lw = 0.8, ls = "--")
                ax.set_title("{} - {}".format(title, i), loc = "left")
                ax.set_xlabel("Ano")
                ax.set_ylabel("SPI")
                ax.set_ylim(ylim[0], ylim[1])
                fig.savefig(
                    "{}/Figuras/{}_{}".format(os.getcwd(), fig_name, i),
                    dpi = 600, bbox_inches = "tight", facecolor = "w")
                plt.close()
#%%
spi12 = pd.read_csv("{}/Dados/SPI12-Dez.csv".format(os.getcwd()), sep = ";", header = None, index_col = 0).T
band1 = pd.read_csv("{}/Dados/band1.csv".format(os.getcwd()), sep = ";", header = None, index_col = 0).T
band2 = pd.read_csv("{}/Dados/band2.csv".format(os.getcwd()), sep = ";", header = None, index_col = 0).T
band3 = pd.read_csv("{}/Dados/band3.csv".format(os.getcwd()), sep = ";", header = None, index_col = 0).T
shp = gpd.read_file("{}/Shapes/BR_UF_2020.shp".format(os.getcwd()))

#%%
if (spi12.iloc[:,:2].equals(band1.iloc[:,:2])) & (band1.iloc[:,:2].equals(band2.iloc[:,:2])) & (band2.iloc[:,:2].equals(band3.iloc[:,:2])) :
    coords = spi12.iloc[:,:2]
else:
    print("Coordenadas divergem entre os dataframes")

#%%
spi_df = spi12.iloc[:,2:]
b1_df = band1.iloc[:,2:]
b2_df = band2.iloc[:,2:]
b3_df = band3.iloc[:,2:]

#%%
kmeans_SPI = KMeans(n_clusters = 7, random_state = 0)
kmeans_SPI.fit(spi_df)
center_SPI = pd.DataFrame(kmeans_SPI.cluster_centers_).T
center_SPI = rename_columns(center_SPI) 
center_SPI.insert(0, "Ano", range(1950, 2016 + 1))
cluster_SPI = pd.DataFrame({"lon": coords["x"], "lat": coords["y"], "Class": kmeans_SPI.labels_})
center_SPI.to_csv(
    "{}/Dados/SPI12_Center.csv".format(os.getcwd()),
    sep = ";", header = True, index = False)

kmeans_b1 = KMeans(n_clusters = 7, random_state = 0)
kmeans_b1.fit(b1_df)
center_b1 = pd.DataFrame(kmeans_b1.cluster_centers_).T
center_b1 = rename_columns(center_b1) 
center_b1.insert(0, "Ano", range(1950, 2016 + 1))
cluster_b1 = pd.DataFrame({"lon": coords["x"], "lat": coords["y"], "Class": kmeans_b1.labels_})
center_b1.to_csv(
    "{}/Dados/Band1_Center.csv".format(os.getcwd()),
    sep = ";", header = True, index = False)

kmeans_b2 = KMeans(n_clusters = 5, random_state = 0)
kmeans_b2.fit(b2_df)
center_b2 = pd.DataFrame(kmeans_b2.cluster_centers_).T
center_b2 = rename_columns(center_b2) 
center_b2.insert(0, "Ano", range(1950, 2016 + 1))
cluster_b2 = pd.DataFrame({"lon": coords["x"], "lat": coords["y"], "Class": kmeans_b2.labels_})
center_b2.to_csv(
    "{}/Dados/Band2_Center.csv".format(os.getcwd()),
    sep = ";", header = True, index = False)

kmeans_b3 = KMeans(n_clusters = 3, random_state = 0)
kmeans_b3.fit(b3_df)
center_b3 = pd.DataFrame(kmeans_b3.cluster_centers_).T
center_b3 = rename_columns(center_b3) 
center_b3.insert(0, "Ano", range(1950, 2016 + 1))
cluster_b3 = pd.DataFrame({"lon": coords["x"], "lat": coords["y"], "Class": kmeans_b3.labels_})
center_b3.to_csv(
    "{}/Dados/Band3_Center.csv".format(os.getcwd()),
    sep = ";", header = True, index = False)

#%%
dict_scatter = [
    {"Class": 0, "color": "green", "label": "Cluster 1"},
    {"Class": 1, "color": "red", "label": "Cluster 2"},
    {"Class": 2, "color": "blue", "label": "Cluster 3"},
    {"Class": 3, "color": "darkorange", "label": "Cluster 4"},
    {"Class": 4, "color": "black", "label": "Cluster 5"},
    {"Class": 5, "color": "darkmagenta", "label": "Cluster 6"},
    {"Class": 6, "color": "darkcyan", "label": "Cluster 7"}
]
#%%
spatial_plot(cluster_SPI, shp, dict_scatter, "a) SPI12-Dez", "SPI12-Dez")
spatial_plot(cluster_b1, shp, dict_scatter, "b) Banda 1 (2 até 8 anos)", "Banda_1")
spatial_plot(cluster_b2, shp, dict_scatter, "c) Banda 2 (9 até 40 anos)", "Banda_2")
spatial_plot(cluster_b3, shp, dict_scatter, "d) Banda 3 (40+ anos)", "Banda_3")

#%%
center_plot(center_SPI, dict_scatter, "SPI12-Dez", "SPI12-Dez", [-3.3, 3.3])
center_plot(center_b1, dict_scatter, "Banda 1", "Banda_1", [-3, 3])
center_plot(center_b2, dict_scatter, "Banda 2", "Banda_2", [-0.8, 0.8])
center_plot(center_b3, dict_scatter, "Banda 3", "Banda_3", [-1.2, 0.5])
# %%
