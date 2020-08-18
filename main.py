from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
@app.route('/demestic_trend')
def demestic_trend():
    return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

# 通过flask 展示疫情数据
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)