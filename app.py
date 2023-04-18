from flask import Flask,render_template
import requests

app=Flask(__name__)


@app.route('/index')
def llamar_templates():
    
    return render_template('index_a_copy.html')

@app.route('/docs')
def docs():
    return render_template('documentacion.html')

@app.route('/prueba')
def prueba():
    json_final= requests.get(url= 'http://127.0.0.1:8000/penitenciarias').json()
    return render_template('prueba.html', json_final=json_final)

if __name__ == '__main__':
    app.run(debug=True)