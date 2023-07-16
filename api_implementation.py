
import json 
import requests

url = 'http://127.0.0.1:8000/tempo_predict'

input_data_for_model = {
    'Film_Animation' :0,
    'Music':1,
    'Sports': 0,
    'Subscriptores': 2,
    'comment_count_dur': 1,
    'view_count_dur': 3,
    'trending_dur':1,
    'Status': 0
}

input_json=json.dumps(input_data_for_model)

response = requests.post(url,data=input_json)

print(response.text)