from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Loading the saved model
sobrevivencia_model = pickle.load(open('/home/brayan/Documents/pandas_20/model_3.sav', 'rb'))

def model_a(lista):
    colunas = ['Film & Animation', 'Music', 'Sports', 'Subscriptores', 'comment_count_dur', 'view_count_dur',
               'trending_dur', 'Status']
    input_data_array = np.array(lista)
    df = pd.DataFrame(data=input_data_array.reshape(1, -1), columns=colunas)
    return sobrevivencia_model.predict_median(df).item()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_list = [
            int(request.form['Film_Animation']),
            int(request.form['Music']),
            int(request.form['Sports']),
            float(request.form['Subscriptores']),
            float(request.form['comment_count_dur']),
            float(request.form['view_count_dur']),
            float(request.form['trending_dur']),
            int(request.form['Status'])
        ]
        prediction = model_a(input_list)
        return render_template('index.html', prediction=prediction)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
