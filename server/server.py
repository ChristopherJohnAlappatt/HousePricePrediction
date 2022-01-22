from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    location = request.form['location']
    sqft = request.form['total_sqft']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction ....")
    util.load_saved_artifacts()
    app.run()
