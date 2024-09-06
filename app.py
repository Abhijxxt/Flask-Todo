from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.String(length=200), nullable=False)

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def HomePage():
    if request.method == 'GET':
        todo_data = Todo.query.all()
        return render_template('home.html', todos=todo_data)
    else:
        todo_message = request.form['todo']
        todo_model = Todo(message=todo_message)
        try:
            db.session.add(todo_model)
            db.session.commit()
            return redirect('/')
        except:
            return "Error Occured"

@app.route('/delete/<int:id>')
def deletePage(id):
    try:
        delete_todo = Todo.query.get_or_404(id)
        db.session.delete(delete_todo)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an error deleting message"

if __name__ == '__main__':
    app.run(debug=True)