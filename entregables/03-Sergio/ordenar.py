#%%
import pandas as pd
df = pd.read_csv("data.csv")


df_ordenado = df.sort_values(by='vote_count', ascending=True)

df_ordenado.to_csv("data_ordenado.csv", index=False)