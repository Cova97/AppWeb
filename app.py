from flask import Flask, render_template, request, redirect

app = Flask(__name__)

url = 'https://api-flask-6939.onrender.com/api/alumnos'

app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        pass

if __name__ == "__mian__":
    app.run(debug = True)