import json
from flask import Flask, render_template,request,redirect,url_for
import metodos as m
app = Flask(__name__)

respuestas = ['Son dos cosas distintas. El Alzheimer es un tipo de demencia. Que es para mí la demencia, lo que para todo el mundo debería ser una enfermedad degenerativa que va afectando la memoria y otras funciones intelectuales más. Pero si tú me preguntas más ya sentimentalmente que es la demencia, es la importancia de tener familia.',
'Es una enfermedad tremendamente difícil, es una enfermedad yo no sé, catastrófica realmente. Deteriorante socialmente, con una progresión paulatina'
'Es algo triste, porque es donde la persona pierde su yo, su autonomía y si es verdad ellos se enfocan en otro mundo, ellos ya no van a sufrir realmente, el que va a sufrir es el cuidador,',
'Grupo de enfermedades o un grupo de síndromes caracterizados por eso, por la neuro-degeneración, por la disminución de la reserva cognitiva, de la reserva neurológica.']



@app.route('/')
def _():
  return render_template('home.html')

@app.route('/cargar')
def _cargar_():
  temp=[]
  for r in respuestas:
    temp.append(m.metodo(r))
  return json.dumps({'data':temp}),200,{'Content-Type': 'application/json'}

@app.route('/cj', methods = ['GET'])
def _cj():
  return m.metodo(request.values.get('frase')),200,{'Content-Type': 'application/json'}

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True) 