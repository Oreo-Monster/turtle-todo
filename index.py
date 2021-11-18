import flask
from todolist import todolist

app = flask.Flask(__name__)
todoList = todolist()

@app.route('/')
def index():
    return flask.redirect('/todo')


@app.route('/todo')
def todo():
    todoList_html = todoList.toHTML()
    return flask.render_template('index.html', todos=todoList_html)

@app.route('/delete/<int:idx>')
def delete(idx):
    if idx >= 0 and idx < todoList.getSize():
        todoList.remove(idx)
    return flask.redirect(f'/todo')

@app.route('/add', methods=["POST"])
def add():
    todo_text = flask.request.form.get("todo_text", default="Missed")
    priorety = flask.request.form.get("priorety", default="Missed")
    todoList.addTask(todo_text, priorety)
    return flask.redirect(f'/todo')

@app.route('/check/<int:idx>', methods=["POST"])
def check(idx):
    todoList.check(idx)
    return flask.redirect(f'/todo')
    
if __name__ == "__main__":
    app.run(debug=True)