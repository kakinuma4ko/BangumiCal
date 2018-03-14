from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bgm/<id>')
def hello(id=None):
    import requests
    bgm_api_url = 'https://api.bgm.tv'
    url = bgm_api_url+"/subject/"+id
    res = requests.get(url)
    return render_template('bgm.html', id=res.json()['name'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
