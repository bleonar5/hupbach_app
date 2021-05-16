from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ntxvgjsrgmukai:df709e8c9cc1af4041141cdc10ca555cef280614c02389c8351a1a20e4eb2cbe@ec2-34-200-94-86.compute-1.amazonaws.com:5432/df3oaej4nh7fsf'

db = SQLAlchemy(app)

from models import User

@app.route('/add/')
def webhook():
    u = User(pid = request.args.get('pid'), object_type = request.args.get('object_type'), version = request.args.get('version'), reactivation = request.args.get('reactivation'))#group = int(request.args.get('group')), key_order = 0)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

@app.route('/get/')
def delete():
    u = User.query.filter(User.pid == str(request.args.get('pid'))).first()
    #db.session.delete(u)
    #db.session.commit()
    return jsonify({
        'group':u.group})

@app.route('/redirect/s1')
def sl():
    u = User.query.filter(User.pid == str(request.args.get('pid'))).first()
    if u:
        return(redirect('https://app.prolific.co/submissions/complete?{}'.format(request.args.get('completion_code'))))
    else:
        u = User(pid = request.args.get('pid'), object_type = request.args.get('object_type'), version = request.args.get('version'))
        print("user created", u)
        db.session.add(u)
        db.session.commit()
        return(redirect('https://app.prolific.co/submissions/complete?cc={}'.format(request.args.get('completion_code'))))

@app.route('/redirect/s2')
def s2():
    u = User.query.filter(User.pid == str(request.args.get('PROLIFIC_PID'))).first()
    url = 'https://blc20.iad1.qualtrics.com/jfe/form/SV_8kSbch15uEldXOm'
    if u:
        return(redirect('{}?PROLIFIC_PID={}object_type={}&version={}'.format(url,u.pid,u.object_type,u.version)))
    else:
        return 'We do not have a record for your prolific ID. Please contact experiment administrator'

@app.route('/redirect/s2/end')
def s2_end():
    u = User.query.filter(User.pid == str(request.args.get('pid'))).first()
    if u:
        u.reactivation = request.args.get('reactivation')
        db.session.commit()
        print("user updated", u)
        return(redirect('https://app.prolific.co/submissions/complete?cc={}'.format(request.args.get('completion_code'))))
    else:
        return 'We do not have a record for your prolific ID. Please contact experiment administrator'

@app.route('/redirect/s3')
def s3():
    u = User.query.filter(User.pid == str(request.args.get('pid'))).first()
    if u.object_type == 'Beach':
        url = 'https://blc20.iad1.qualtrics.com/jfe/form/SV_9WAElYt5wP956e2'
    elif u.object_type == 'Neutral':
        url = 'https://blc20.iad1.qualtrics.com/jfe/form/SV_7QimFdKbTh0fMDI'
    else:
        url = 'https://blc20.iad1.qualtrics.com/jfe/form/SV_0961peJgVtIvuh8'
    if u:
        return(redirect('{}?PROLIFIC_PID={}&object_type={}&version={}&reactivation={}'.format(url,u.pid,u.object_type,u.version,u.reactivation)))
    else:
        return 'We do not have a record for your prolific ID. Please contact experiment administrator'


if __name__ == '__main__':
    app.run()
