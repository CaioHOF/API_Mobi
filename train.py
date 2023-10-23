import pandas as pd
# import uuid
import joblib
from sklearn.cluster import KMeans

K = 100
FILE_PATH = 'data.csv'
MODEL_PATH = 'model.pkl'

# def add_uuid(df):
#   uuid_col = [uuid.uuid4() for _ in range(len(df))]
#   df["uuid"] = uuid_col
#   return(df)

def train(df,k):
  cols = ["altura", "largura", "profundidade", "peso", "L_imagem"]
  kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(df[cols])
   
  joblib.dump(kmeans, MODEL_PATH)
  # df = add_uuid(df)
  df['predict'] = kmeans.labels_
  df.to_csv(FILE_PATH, index=False)

if __name__ == '__main__':
    df = pd.read_csv(FILE_PATH)
    # df = df.drop(["nome","image_url"], axis=1)
    train(df, K)
