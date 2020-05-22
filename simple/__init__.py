import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    output = ""
    for k, v in os.environ.items():
        output = output + f'{k}={v}  <br />'

    return output
    
@app.route('/set')
def set():
    """Renders the set page."""
    k = request.args.get("key")
    v = request.args.get("value")
    # how to set 
    os.environ[k] = v
    
    return f"{k}={v}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
