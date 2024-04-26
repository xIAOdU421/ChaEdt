import json


with open('./settings.json','r') as f:
    settingDatas = json.load(f)

keys = settingDatas['keys']

render_range = settingDatas['render_range']