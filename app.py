from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

#@app.route("/")
#def home():
#    return "Hello, Flask!"

models = joblib.load('model1.joblib')

@app.route("/get-simmilar-reccomendation", methods=['POST'])
def print_similar_drama():
    # title
    title = request.form.get('judul')
    if not title:
        return "No title provided"

    prediction = models.predict([title])

    # TODO: get sinopsis and year in this function, using dataframe
    return prediction

if __name__ == "__main__":
    app.run()