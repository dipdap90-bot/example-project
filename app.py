#app.py
from flask import Flask,render_template
# from dotenv import load_dotenv
import os

# load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    api_key = os.getenv('FLIGHT_API')
    return render_template('predict.html', result=api_key)

if __name__ == '__main__':
    app.run(debug=True)