from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def HomePage():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        todo_message = request.form['todo']
        print(todo_message)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)