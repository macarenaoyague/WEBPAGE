from flask import Flask, render_template, request, session, Response
from sqlalchemy import and_
from sqlalchemy import or_
from model import entities
from database import connector
import json
import datetime

app = Flask(__name__)
db = connector.Manager()
engine = db.createEngine()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    if 'logged_user' in session:
        return render_template('profile.html')
    else:
        return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    Username = request.form['Username']
    Password = request.form['Password']
    session = db.getSession(engine)
    users = session.query(entities.User)
    for user in users:
        if user.username == Username and user.password == Password:
            return render_template('home.html')
    return render_template('login.html')

@app.route('/sign_up', methods=['GET'])
def sign_up():
    return render_template("sign_up.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

@app.route('/home')
def logout():
    session.clear()
    return render_template('index.html')




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
