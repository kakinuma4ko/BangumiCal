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
    url = bgm_api_url+'/subject/219200'+'?responseGroup=large'
    bgm_json = requests.get(url).json()
    bgm_date = []
    for ep in bgm_json['eps']:
        bgm_date.append(ep['airdate'])
    print bgm_date
    return render_template('bgm.html', con='1')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
