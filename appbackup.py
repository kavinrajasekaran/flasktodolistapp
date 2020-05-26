from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from task import Task
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kavinrajasekaran/Documents/CSP/flask/todo/todo3.db'

db = SQLAlchemy(app)
#events = ["Spring Visit", "On May 1st at Donlon from 1:30 to 2:30"]

class Event(db.Model):


    id =  db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.Text)
    task_description = db.Column(db.Text)
    task_priority = db.Column(db.Text)
    task_completion = db.Column(db.Text)

@app.route("/")
def root():
    events = Event.query.all()
    return redirect(url_for('index', events = events))


@app.route('/events', methods = ["GET","POST"])
def index():
    if request.method == "POST":

        new_task = Event(task_name = request.form['task_name'], task_description =  request.form['task_description'], task_priority = request.form['task_priority'], task_completion = request.form['task_completion'])
        #events.append(new_task)
        db.session.add(new_task)
        db.session.commit()

        return redirect (url_for('index'))
    return render_template('index.html', events = Event.query.all())

@app.route('/events/<int:id>', methods = ["GET","PATCH","DELETE"])
def show(id):
    found_task = Event.query.get(id)
    if request.method == b'PATCH':
        found_task.task_name = request.form['t_name']
        found_task.task_description = request.form['t_description']
        found_task.task_priority = request.form['t_priority']
        found_task.task_completion = request.form['t_completion']
        db.session.add(found_task)
        db.session.commit()

        return redirect(url_for('index'))

    if request.method == b'DELETE':
        db.session.delete(found_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('show.html', event = found_task)

@app.route('/events/<int:id>/edit')
def edit(id):
    found_task = Event.query.get(id)
    return render_template('edit.html', event = found_task)

@app.route('/events/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5001)
