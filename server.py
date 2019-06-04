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

@app.route('/view/<content>')
def static_content(content):
    return render_template(content)

#login
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

#signup
@app.route('/sign_up', methods=['GET'])
def sign_up():
    return render_template("sign_up.html")

#logout
@app.route('/home')
def logout():
    session.clear()
    return render_template('index.html')

#subject
@app.route('/subjects', methods = ['GET'])
def get_subject():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Subject)
    data = []
    for message in dbResponse:
        data.append(message)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/subjects', methods = ['POST'])
def create_subject():
    c =  json.loads(request.form['values'])
    session = db.getSession(engine)
    message = entities.Subject(
        name_subject=c['name_subject'],
        career_from_id=c['career_from_id']
    )
    session.add(message)
    session.commit()
    return 'Created Subject'

@app.route('/subjects', methods = ['PUT'])
def update_subject():
    session = db.getSession(engine)
    id = request.form['key']
    message = session.query(entities.Subject).filter(entities.Subject.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(message, key, c[key])
    session.add(message)
    session.commit()
    return 'Updated Subject'

@app.route('/subjects', methods = ['DELETE'])
def delete_subject():
    id = request.form['key']
    session = db.getSession(engine)
    messages = session.query(entities.Subject).filter(entities.Subject.id == id)
    for message in messages:
        session.delete(message)
    session.commit()
    return "Deleted Subject"

#career
@app.route('/careers', methods = ['GET'])
def get_career():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Career)
    data = []
    for message in dbResponse:
        data.append(message)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/careers', methods = ['POST'])
def create_career():
    c =  json.loads(request.form['values'])
    session = db.getSession(engine)
    message = entities.Career(
        name_career=c['name_career']
    )
    session.add(message)
    session.commit()
    return 'Created Subject'

@app.route('/careers', methods = ['PUT'])
def update_career():
    session = db.getSession(engine)
    id = request.form['key']
    message = session.query(entities.Career).filter(entities.Career.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(message, key, c[key])
    session.add(message)
    session.commit()
    return 'Updated Subject'

@app.route('/careers', methods = ['DELETE'])
def delete_career():
    id = request.form['key']
    session = db.getSession(engine)
    messages = session.query(entities.Career).filter(entities.Career.id == id)
    for message in messages:
        session.delete(message)
    session.commit()
    return "Deleted Subject"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
