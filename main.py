from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import generativeai
import os

app = Flask(__name__)

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    model = generativeai.GenerativeModel('gemini-1.0-pro-latest')
    generativeai.configure(api_key=os.getenv('API'))
    contex = 'Responda como se fosse um ser oniciente que sabe de tudo'
    prompt = request.args.get('prompt')
    input_ia = f'{contex}: {prompt}'
    outpot = model.generate_content(input_ia)
    return {'message': outpot.text}

if __name__ == '__main__':
    app.run(debug=True)

