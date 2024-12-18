# from flask import Flask, redirect, url_for, request # type: ignore

# app = Flask(__name__)

# # data = []

# @app.route('/success/<name>')
# def success(name):
#     return 'Welcome %s!' % name

# @app.route('/login', methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         name = request.form.get['name']
#         # age = request.form.get['age']
#         # data.append({'name': name, 'age': age})
#         return redirect(url_for('success', name=name))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=name))
#     # return render_template('login.html', data=data)

# # @app.route('/success/<name>/<age>')
# # def success(name,age):
# #         name = request.args.get('name')
# #         age = request.args.get('age', default=None, type=int)
# #         return f'Welcome, {name}! You are {age} years old.'
    
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)