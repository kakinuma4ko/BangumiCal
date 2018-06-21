import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bgm/<id>')
def hello(id=id):
    import requests
    bgm_api_url = 'https://api.bgm.tv'
    url = bgm_api_url+'/subject/'+str(id)+'?responseGroup=large'
    bgm_json = requests.get(url).json()
    # print json.dumps(bgm_json, sort_keys=True, indent=4)
    with open("./test.json",'w') as json_file:
         json.dump(bgm_json,json_file,ensure_ascii=True)
    # bgm_date = []
    # for ep in bgm_json['eps']:
    #     bgm_date.append(ep['airdate'])
    return render_template('bgm.html', name=bgm_json['name'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
