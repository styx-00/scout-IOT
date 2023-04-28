from flask import Flask, render_template,request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/change', methods=['POST'])
def parse_request():
    data=request.get_json()
    print(data)
    return 
@app.route('/about')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
#curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/change