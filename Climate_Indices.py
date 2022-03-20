#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
#%%

dict_index = {        
    "Nino": "https://psl.noaa.gov/data/correlation/nina34.anom.data",
    "PDO": "https://psl.noaa.gov/data/correlation/pdo.data",
    "AMO": "https://psl.noaa.gov/data/correlation/amon.us.data",
    "TNA": "https://psl.noaa.gov/data/correlation/tna.data",
    "TSA": "https://psl.noaa.gov/data/correlation/tsa.data"
    }


#%%
index_df = pd.DataFrame({"Ano": [], "Mes": []})
for key, value in dict_index.items():

    url_data = requests.get(dict_index[key]).text
    index_table = re.sub(" +", " ", url_data).replace(" ", ";")
    index_list = []
    for line in iter(index_table.split("\n")[1:]):
        if "-9" not in line[0:4]:
            index_list.append(line)
        else:
            break
    df = pd.DataFrame({key:index_list})[key].str.split(";", expand = True)
    if key != "PDO":
        df.drop(df.columns[0], axis = 1, inplace = True)
        df.columns = df.columns-1
    else:
        df.drop(df.columns[-1], axis = 1, inplace = True)
    df.apply(pd.to_numeric)       
    index_ts = pd.melt(df, id_vars = df.columns[0])
    index_ts.columns = ["Ano", "Mes", key]
    index_ts.sort_values(by = ["Ano", "Mes"], inplace = True)
    index_ts.reset_index(inplace = True, drop = True)
    index_df = index_df.merge(index_ts, how = "outer", on = ["Ano", "Mes"])

index_df.to_csv("{}/Dados/Climate_Indices.csv".format(os.getcwd()), sep = ";", header = True, index = False)
# %%
