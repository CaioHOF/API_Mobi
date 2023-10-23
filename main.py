
from flask import Flask, request, render_template
from predict import recomendacao

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    solution = None
    if request.method == 'POST':

      peso  = float(request.form.get('peso'))
      largura  = float(request.form.get('largura'))
      comprimento  = float(request.form.get('comprimento'))
      profundidade  = float(request.form.get('profundidade'))
      L_imagem = 223270777
      
      solution = recomendacao(peso, largura, comprimento, profundidade, L_imagem)
     
      return render_template('index.html', solution=solution)
    else:
        return render_template('index.html', solution=solution)
if __name__ == '__main__':
    app.run(debug=True)