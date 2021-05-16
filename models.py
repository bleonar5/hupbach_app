from manage import db,app

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	pid = db.Column(db.String(64),index=True,unique=True)
	object_type = db.Column(db.String(64))
	version = db.Column(db.String(64))
	reactivation = db.Column(db.String(64))

	def __init__(self,pid,object_type,version,reactivation):
		self.pid = pid
		self.object_type = object_type
		self.version = version
		self.reactivation = reactivation

	def __repr__(self):
		return '<User %r>' % (self.pid)
