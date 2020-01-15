from app import db
from app.models import User, Task
Task.query.delete()
User.query.delete()

# create a user object
user = User(username="AArgher")

# add the user to the session and save (commit)
db.session.add(user)
db.session.commit()

# get all the users in the DB (in this case, there is only one user)
users = User.query.all()
print(users)
user = users[0]
print("User Id: {} \nUser name: {}.".format(user.id, user.username))

user = User.query.get(1)
print("User Id: {} \nUser name: {}.".format(user.id, user.username))


task1 = Task(title='Jump up and down', description="In anger, in joy", done=True, user=user)
task2 = Task(title='Crawl', description="Front or back", user=user)
db.session.add(task1)
db.session.add(task2)
db.session.commit()
task1 = Task.query.get(1)
print(task1.title)
task2 = Task.query.get(2)
print(task2.title)
tasks = Task.query.all()
print(tasks)

task_user = Task.query.get(1).user
print(task_user.username)

user_tasks = User.query.get(1).tasks.all()
print(user_tasks)
