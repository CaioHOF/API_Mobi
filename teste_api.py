# -*- coding: utf-8 -*-
"""TESTE_API

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n64sgu8WutCaIAvjfLuq_8XiTVrPd7U3
"""

import pandas as pd
import random
import uuid
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv()


# Inicialize o codificador OneHotEncoder
encoder = OneHotEncoder(sparse = False)

# Ajuste e transforme os códigos de material e cor usando o codificador
cor_encoded = encoder.fit_transform(df[["cor"]])

# Crie um DataFrame a partir da matriz de saída codificada
cor_encoded_df = pd.DataFrame(cor_encoded,
                                       columns=encoder.get_feature_names_out(["cor"]))

# Concatene o DataFrame codificado com o DataFrame original
df_encoded = pd.concat([df.drop(["cor"], axis=1), cor_encoded_df], axis=1)



# Continue com o seu código de clustering K-Means...
kmeans = KMeans(n_clusters=10, random_state=0, n_init="auto").fit(df_encoded)


kmeans.cluster_centers_

df_encoded['predict'] = kmeans.labels_

uuid_col = [uuid.uuid4() for _ in range(500)]

# Adicione o UUID à lista de colunas
df_encoded["uuid"] = uuid_col
def recomendacao(cor, largura, comprimento, profundidade):

  data = {
    "cor": [cor],
    "largura":[largura],
    "comprimento": [comprimento],
    "profundidade": [profundidade]
  }

  # Crie o DataFrame
  df_temp = pd.DataFrame(data)

  cor_encoded = encoder.transform(df_temp[["cor"]])
  cor_encoded_df_temp = pd.DataFrame(cor_encoded, columns=encoder.get_feature_names_out(["cor"]))
  df_temp_encoded = pd.concat([df_temp.drop(["cor"], axis=1), cor_encoded_df], axis=1)

  class_predict = kmeans.predict([df_temp_encoded.iloc[0]])
  filter = df_encoded[df_encoded['predict'] == class_predict[0] ]['uuid']
  return filter