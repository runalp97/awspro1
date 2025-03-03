
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return jsonify({"message": "new developer came 3rd change pushed this is the complete pipeline!"})

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=PORT)
