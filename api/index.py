# Flask application
from flask import Flask, request, jsonify, render_template
from api import util

app = Flask(__name__, template_folder='../templates')  # Point to the templates folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.form
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({'estimated_price': estimated_price})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Flask Server...")
    util.load_saved_artifacts()
    app.run(debug=True)
