from . import db

class movies(db.Model):
    __tablename__='movies'
    id = db.Column(db.Integer, primary_key=True) #, unique=True
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at
        
    def __repr__(self):
        return '<movies %r>' % (self.title)

""" 
class plz(db.Model):
    __tablename__='plz'
    id = db.Column(db.Integer,primary_key=True)
    poster = db.Column(db.String(82))

    def __init__(self, poster):
        self.poster = poster
"""



