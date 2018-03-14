import requests
bgm_api_url = 'https://api.bgm.tv'
url = bgm_api_url+"/subject/219200"
res = requests.get(url)
print res,res.json()