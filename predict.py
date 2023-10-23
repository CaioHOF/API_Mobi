import joblib
import pandas as pd

MODEL_PATH = 'model.pkl'
FILE_PATH = 'data.csv'

model = joblib.load(MODEL_PATH)
df = pd.read_csv(FILE_PATH)
def recomendacao(peso, largura, comprimento, profundidade, L_imagem):

  data = {
    "peso": [peso],
    "largura":[largura],
    "comprimento": [comprimento],
    "profundidade": [profundidade],
    "L_imagem": [L_imagem]
  }

  df_temp = pd.DataFrame(data)

  class_predict = model.predict([df_temp.iloc[0]])
  filter = list(df[df['predict'] == class_predict[0] ]['image_url'])
  return filter
  
