import pandas as pd
from sklearn.neighbors import NearestNeighbors


ds_filmes = pd.read_csv('movies.csv')
# print(ds_filmes)

ds_ratings = pd.read_csv('ratings.csv')
# print(ds_ratings)
ds_ratings = ds_ratings[['userId','movieId','rating']]

df = pd.merge(ds_filmes,ds_ratings, on='movieId')

#print(df)

df_recommender = df.pivot_table(index='userId',columns='title', values='rating').fillna(0)

# print(df_recommender)

modelo_knn = NearestNeighbors(metric='cosine')
modelo_knn.fit(df_recommender)

idx_usuario = 230
distancia, indices_vizinhos = modelo_knn.kneighbors(df_recommender.iloc[idx_usuario].values.reshape(1,-1), n_neighbors=3)

usuario = df_recommender.index[idx_usuario]

for i in range(0, len(distancia.flatten())):
    if i==0:
        print(f"Usuário: {usuario}")
    else:
        print(f"Vizinho {df_recommender.index[indices_vizinhos.flatten()[i]]}, com distância de {distancia.flatten()[i]}")

ds_usuario = df_recommender.loc[usuario].to_frame()
vizinho_proximo = df_recommender.index[indices_vizinhos.flatten()[1]]
ds_vizinho = df_recommender.loc[vizinho_proximo].to_frame()

ds_titulos = pd.merge(ds_usuario, ds_vizinho, on='title').sort_values(by=vizinho_proximo, ascending=False)

ds_titulos = ds_titulos[(ds_titulos[vizinho_proximo] > 0) & (ds_titulos[usuario] == 0)].reset_index()

print(ds_titulos.head(5))
print('\n')

print(list(ds_titulos.title[:5]))






