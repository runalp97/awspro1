from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return jsonify({"message": "now that the pipeline has been made the 2nd developer wants some schnage in code this is the new code pipeline will again start!"})

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=PORT)
