from . import db


class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User{self.username}''
