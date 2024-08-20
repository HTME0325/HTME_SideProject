from flask import Flask, request, jsonify, render_template
import requests as req
import math

### 初始化 Flask
app = Flask(__name__)
app.json.ensure_ascii = False 


@app.route('/', methods=['GET'])
def index():
    return render_template('index_youbike.html')

@app.route('/youbike_taipei', methods = ['GET'])
def get_youbike_location_in_taipei():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    res = req.get(url)
    return jsonify(res.json())






### 啟動網站
if __name__ == "__main__":
    app.run(
        debug = True,
        host = '127.0.0.1',
        port = 5000
    )