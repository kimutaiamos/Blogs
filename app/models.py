from _typeshed import Self
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
    


    @property
    def password(self):
        raise AttributeError("you cannot read the attribute password")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #creating the user logic
    def unlike_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id = self.id, post_id  = post.id)
            db.session.add(like)

    #creating user dislike logic
    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id = self.id,
                post_id = post.id).delete()

    #checking if user liked the post
    def has_liked_post(self, post):
        return PostLIke.query.filter(
            PostLike.user_id ==self.id,
            PostLike.post_id == post.id).count() > 0

    #string to print out a row of column important in debugging
    def __repr__(self):
        return f"User {self.username}"
       
