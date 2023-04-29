from flask import Flask, render_template,request
import json

app = Flask(__name__)
global raw
raw=b'name=johith'
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/change', methods=['POST'])
def parse_request():
    global raw
    raw=request.get_data()
    print(raw)
    print("the client data is "+ raw.decode())
    return 'data received'

#Fetch api endpoint
#Dynamic Redendering

@app.route('/fetchChange',methods=['GET'])
def fetchChange():
    global raw
    # return converter(raw)
    return converter(raw)

#convert x-www-form-urlencoded to json
def converter(raw_data):
    str=raw_data.decode()
    param=str.split('&')
    print(param)
    global dict
    dict={}
    for i in param:
        temp=i.split('=')
        dict[temp[0]]=temp[1]
    return dict


# @app.route('/about')
# def about():
#     return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
#curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/change