from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pass default values for name and age
    return render_template('index.html', name=None, age=None)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '')
    age = request.form.get('age')

    # Ensure age is converted to integer if provided, else set to None
    try:
        age = int(age)
    except (ValueError, TypeError):
        age = None

    return render_template('index.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
