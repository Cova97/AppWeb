from flask import Flask, render_template, redirect, request, abort
import requests

app = Flask(__name__)

url = 'https://api-flask-6939.onrender.com/api/alumnos'

app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        alumnos = request.get(url).json()['Alumnos']
        completed = []
        incompleted = []
        for task in task:
            if task['status'] == True:
                completed.append(task)
            else:
                incompleted.append(task)
        print(f'COMPLETAS: {completed}')
        print(f'INCOMPLETAS: {incompleted}')
        #print(alumnos)
        response = {'completed': completed,
                    'incompleted': incompleted,
                    'counter1': len(completed),
                    'counter2': len(incompleted)}
        return render_template('index.html', response = response)
    else:
        name = request.form['name']
        try:
            requests.post(url, json={'name': name})
            return redirect('/')
        except:
            return abort(500)

if __name__ == "__mian__":
    app.run(debug = True)