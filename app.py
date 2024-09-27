# app.py
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '')
    age = request.form.get('age')
    return render_template('index.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
