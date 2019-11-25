from flask import Flask
from flask import render_template
from resource.room import ClassRoom
import time

app = Flask(__name__)

app.config['DEBUG'] = True
app.secret_key = 'TcDrS24hYddPExwMTfdM7d2Y'

@app.route('/')
def index():
    return 'Go to /classroom/<string:salon_nro>'

@app.route('/classroom/<string:classroom_nro>')
def room(classroom_nro=None):
    result = ClassRoom.getActualClass(classroom_nro)

    if result:
        epoch = result[2]
        inicio = time.strftime("%H:%M", time.gmtime(epoch+60*result[3]))
        fin =  time.strftime("%H:%M", time.gmtime(epoch+60*result[4]))
        descripcion =  result[5].split("::")
        evento = descripcion[0]
        instructor = descripcion[1] if len(descripcion) > 1 else ""
        return render_template('index.html',classroom_nro=classroom_nro, classroom=result,inicio=inicio,fin=fin,evento=evento,instructor=instructor)
    else:
        return render_template('index.html', classroom_nro=classroom_nro, classroom=result, inicio=None, fin=None,evento='Libre', instructor=None)

if __name__ == '__main__':
    app.run(port=5000)
