from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name",methods = ['GET'])
def name():
    data = {
        "name": "Kasey"
    }
    return jsonify(data)

@app.route("/hello/<name>",methods = ['GET'])
def hello(name):
    data = {
        "message": "Hello there,{}".format(name)
    }
    return jsonify(data)

@app.route("/distance", methods = ["POST"])
def distance():
    r = request.get_json()
    d = sqrt((r["b"][0]-r["a"][0])^2 + (r["b"][1]-r["a"][1])^2)

    output = {
        "distance": d,
        "a": [r["a"][0], r["a"][1]],
        "b": [r["b"][0], r["b"][1]]
    }

    return jsonify(output)


if __name__ == "__main__":
    app.run(host="127.0.0.1") 
