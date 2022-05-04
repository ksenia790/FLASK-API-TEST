import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

# Configure table
class Quizz(db.Model):
	__tablename__ = 'quizz'
    
	id = db.Column(db.Integer(),primary_key=True)
	question_id = db.Column(db.Integer(), unique=True)
	answer = db.Column(db.String(100),nullable=False)
	question = db.Column(db.Text(),nullable=False)
	date = db.Column(db.String(100),nullable=False)

	def __repr__(self):
		return self.name

	def save(self):
		db.session.add(self)
		db.session.commit()

db.create_all()