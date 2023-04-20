from flask import Flask,render_template
import requests

app=Flask(__name__)

app.static_folder = "static"

prisiones = requests.get(url="http://127.0.0.1:8000/penitenciarias").json()
@app.route('/')
def llamar_templates():
    # next_id=int(id)+1
    # prev_id=int(id)-1
    return render_template('index_a_copy.html', prisiones=prisiones)

@app.route('/docs')
def docs():
    return render_template('documentacion.html')


@app.route('/documentacion')
def documentacion():
    return render_template('documentacion.html')

if __name__ == '__main__':
    app.run(debug=True)