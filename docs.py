from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/index')
def llamar_templates():
    
    return render_template('index_a_copy.html')

@app.route('/docs')
def docs():
    return render_template('documentacion.html')

if __name__ == '__main__':
    app.run(debug=True)