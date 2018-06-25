import json
from flask import Flask
from flask import render_template, send_file, send_from_directory, make_response

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
    ep_date_list = []
    for ep in bgm_json['eps']:
        ep_date_list.append(ep['airdate'])
    print ep_date_list
    return render_template('bgm.html', name=bgm_json['name'])

@app.route("/ics/<id>", methods=['GET'])
def download_file(id):
    # directory = os.getcwd() 
    file_name = 'kakinuma_test.ics'
    response = make_response(send_from_directory('./', file_name, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
    print 1
    return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost')


