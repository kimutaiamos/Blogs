from enum import unique
from .import db
from werkzeug.security import generate_password_hash, check_password_hash
from .import login_manager
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.column(db.integer,primary_key = True)
    first_name = db.column(db.string(255))
    last_name = db.column(db.string(255))
    username = db.column(db.string(255), unique = True)
    email = db.column(db.string(255), unique = True, index = True)
    bio = db.column(db.string())
    avatar_path = db.column(db.string())
    password_hash = db.column(db.string(255))
    posts = db.relationship("post",
                            backref = "user",
                            lazy = "dynamic")
    comments = db.relationshp("comment",
                                backref = "user",
                                lazy = "dynamic")
    liked = db.relationship("Postlike",
                             backref = "user",
                             lazy = "dynamic")
                             
