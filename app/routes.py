# imports an app object (created in __init__py  Flask(__name__))
from app import app, db 
from flask import render_template
from app.models import User, Task

@app.route("/tasks")
def index():
    user= User.query.get(1)
    tasks = user.tasks
    return render_template('index.html', title='Home', user=user, tasks=tasks)

@app.route('/tasks', methods=['POST'])
def create():
    user= User.query.get(1)
    return 'Done'

