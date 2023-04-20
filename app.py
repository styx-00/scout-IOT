from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/change', methods=['GET', 'POST'])
def parse_request():
    data=request.data
    print(data)