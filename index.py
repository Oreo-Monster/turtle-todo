import flask
from datetime import datetime
from todolist import todolist
from task import Task
import users as u

currentUser=""
app = flask.Flask(__name__)
todoList = todolist()

@app.route('/')
def index():
    return flask.render_template('login.html',loginerror = 'No users. Please sign up.')

@app.route('/login', methods=["POST"])
def login():
    uname = flask.request.form.get("username", default = "Missed")
    pword = flask.request.form.get("password", default = "Missed")
    if uname not in u.users:
        error = 'Account does not exist. Do you want to make an account?'
        return flask.redirect(flask.url_for('signup'))
    if pword != u.users[uname]:
        error = 'Invalid Credentials. Please try again.'
        return flask.redirect('https://www.youtube.com/watch?v=PlbUYl67LTY')
    elif pword == u.users[uname]:
        global currentUser
        error = 'ur in ^_^'
        currentUser = uname
        return flask.redirect(f'/todo/{uname}')
    error = 'u shouldn-t b here >_<'
    return flask.redirect('https://pokemondb.net/pokedex/charizard')

@app.route('/signup')
def signup():
    #TODO: add signup page
    return "Under construction"


@app.route('/todo/<string:user>')
def todo(user):
    todoList_html = todoList.toHTML()
    return flask.render_template('index.html', todos=todoList_html)

@app.route('/delete/<int:idx>')
def delete(idx):
    if idx >= 0 and idx < todoList.getSize():
        todoList.remove(idx)
        print("Deleted task: " + str(idx))
    return flask.redirect(f'/todo/{currentUser}')

@app.route('/add', methods=["POST"])
def add():
    #TODO still need to scrub the input
    #Also need to check for bad inputs, like empty strings
    #Come back to this to implement tags, priorities, colors, ect.
    todo_text = flask.request.form.get("todo_text", default="Missed")
    priorety = flask.request.form.get("priorety", default="Missed")
    todoList.addTask(todo_text, priorety)
    return flask.redirect(f'/todo/{currentUser}')

@app.route('/check/<int:idx>', methods=["POST"])
def check(idx):
    todoList.check(idx)
    return flask.redirect(f'/todo/{currentUser}')
    
if __name__ == "__main__":
    app.run(debug=True)