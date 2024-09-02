import pandas as pd

creditos = pd.read_csv("tmdb_5000_credits.csv")


print(creditos.head())
print(creditos[['title', 'cast']])
