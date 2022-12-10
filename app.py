from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load('model-recommendation-dramas.joblib')

@app.route("/get-simmilar-recommendation", methods=['POST'])
def get_similar_recommendation():
    # title
    content = request.json
    prediction = model.predict(content['title'])

    # TODO: get sinopsis and year in this function, using dataframe
    return prediction

if __name__ == "__main__":
    app.run()