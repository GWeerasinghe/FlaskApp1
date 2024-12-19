from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("login.html")
database = {'Gayani':'1234', 'James':'5678', 'Nuwani':'0123'}

@app.route('/login', methods=['POST', 'GET'])
def login():
    name = request.form['nm']
    password = request.form['pw']
    if name not in database:
        return render_template('login.html', info='Invalid User..')
    else:
        if database[name]!=password:
            return render_template('login.html', info='Invalid Password.Try Again.')
        else:
            return render_template('home.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)