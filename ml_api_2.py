
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
import json

app = FastAPI()

class model_input(BaseModel):
    Film_Animation: int
    Music: int
    Sports: int
    Subscriptores: float
    comment_count_dur: float
    view_count_dur: float
    trending_dur: float
    Status: int

# Loading the saved model
sobrevivencia_model = pickle.load(open('/home/brayan/Documents/pandas_20/model_3.sav', 'rb'))



def model_a(lista):
    colunas = ['Film & Animation', 'Music', 'Sports', 'Subscriptores', 'comment_count_dur', 'view_count_dur',
               'trending_dur', 'Status']
    input_data_array = np.array(lista)
    df = pd.DataFrame(data=input_data_array.reshape(1, -1), columns=colunas)
    return sobrevivencia_model.predict_median(df).item()






@app.post('/tempo_predict')
def sobrevivencia_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    film = input_dictionary['Film_Animation']
    musi = input_dictionary['Music']
    spor = input_dictionary['Sports']
    subs = input_dictionary['Subscriptores']
    comm = input_dictionary['comment_count_dur']
    view = input_dictionary['view_count_dur']
    tren = input_dictionary['trending_dur']
    stat = input_dictionary['Status']

    input_list = [film, musi, spor, subs, comm, view, tren, stat]
    prediction = model_a(input_list)

    return prediction
