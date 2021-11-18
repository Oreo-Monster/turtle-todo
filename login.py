import users as u
import flask as f
import webbrowser as w

app = f.Flask(__name__, static_folder = "static")
@app.route('/')
def authenticate():
    return f.render_template('login.html',loginerror = 'No users. Please sign up.')

@app.route('/login', methods=["POST"])
def login():
    print('WELCOME')
    uname = f.request.form.get("username", default = "Missed")
    pword = f.request.form.get("password", default = "Missed")
    if f.request.method == 'POST':
        error = 0
       
        if uname not in u.users:
            error = 'Account does not exist. Do you want to make an account?'
            return w.open_new_tab('https://y8.com')
        if uname not in u.users or pword != u.users[uname]:
            print('jbsfkd')
            error = 'Invalid Credentials. Please try again.'
            return f.redirect('https://www.youtube.com/watch?v=PlbUYl67LTY')
        elif pword == u.users[uname]:
            error = 'ur in ^_^'
            return f.render_template('index.html')


        else:
            error = 'u shouldn-t b here >_<'
            return f.redirect('https://pokemondb.net/pokedex/charizard')

        

@app.route('/createuser')
def createacc(username,password):
    u.users[username] = password
    with open("users.py","w") as ulist:
        ulist.write("users = " + str(u.users))


if __name__ == "__main__":
    app.run(debug = True)