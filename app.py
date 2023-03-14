from flask import Flask, render_template, redirect, request, abort
import requests

app = Flask(__name__)

url = 'https://api-flask-g929.onrender.com/items'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        tasks = requests.get(url).json()
        print(tasks)
        response = {'tasks': tasks}
        return render_template('index.html', response = response)
    else:
        abort(505)

if __name__ == "__main__":
    app.run(debug = True)

"""


        completed = []
        incompleted = []
        for item in item:
            if item['status'] == True:
                completed.append(item)
            else:
                incompleted.append(item)
        print(f'COMPLETAS: {completed}')
        print(f'INCOMPLETAS: {incompleted}')
        
        response = {'completed': completed,
                    'incompleted': incompleted,
                    'counter1': len(completed),
                    'counter2': len(incompleted)}
        return render_template('index.html', response = response)


"""

"""
name = request.form['name']
        try:
            requests.post(url, json={'name': name})
            return redirect('/')
        except:
            return abort(500)

"""