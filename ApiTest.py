import requests
# bgm_api_url = 'https://api.bgm.tv'
# url = bgm_api_url+'/subject/219200'+'?responseGroup=large'
# bgm_json = requests.get(url).json()
# for ep in bgm_json['eps']:
#     print ep['airdate'] 

url = 'https://metjm.net/csgo/#S76561198300952829A14185220654D9233155819959642397'
req = requests.get(url)
print req.text