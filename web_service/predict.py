from flask import Flask, jsonify, request
import pickle
import pandas

with open('dict_vect.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

with open("model.pkl", 'rb') as m_in:
    model = pickle.load(m_in)

def prep_features(data):
    df = pandas.DataFrame.from_dict(data)
    dicts = df[['% Iron Concentrate', 'Amina Flow', 'Ore Pulp pH', 'Average Air Flow']].to_dict(orient='records')
    return dicts

def predict(features):

    X = dv.transform(features)
    pred = model.predict(X)
    return pred[0]

app = Flask('ore-quality-prediction')

@app.route('/predict', methods=['POST'])
def predict_end_ppoint():
    conditions = request.get_json()

    features = prep_features(conditions)
    pred = predict(features)

    result = {"% of silica in the ore is": pred}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port=9696)
