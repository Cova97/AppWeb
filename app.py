from flask import Flask, render_template, redirect, request, abort
import requests

app = Flask(__name__)

url = 'https://api-flask-g929.onrender.com/items'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        tasks = requests.get(url).json()
        completed = []
        incompleted  = []
        for task in tasks:
            if task['status'] == True:
                completed.append(task)
            else:
                incompleted.append(task)
        print(f'Tareas Completas: {completed}')
        print(f'Tareas Incompletas: {incompleted}')
        #print(tasks)
        #response = {'tasks': tasks}
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

if __name__ == "__main__":
    app.run(debug = True)



