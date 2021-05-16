from flask import Flask
from flask import request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aojdfyqcvmmslm:1ca0dabf4676f5c7915579909826d4ca508649d8c4baf8c01fb9225a2d5f9ef3@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d86t9tsaptb9be'

db = SQLAlchemy(app)

from models import User

@app.route('/add/')
def webhook():
    u = User(pid = request.args.get('pid'), group = int(request.args.get('group')), key_order = int(request.args.get('key_order')))
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

@app.route('/get/')
def delete():
    u = User.query.filter(User.pid == str(request.args.get('pid'))).first()
    #db.session.delete(u)
    #db.session.commit()
    return Flask.jsonify(u)

if __name__ == '__main__':
    app.run()
