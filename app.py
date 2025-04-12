from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        return jsonify({"error": "Zła liczba"}), 400

    features = {"num1": num1, "num2": num2}
    prediction = 1 if sum(features.values()) > 5.8 else 0

    output = {
        "prediction": prediction,
        "features": features
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
