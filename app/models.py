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
        return PostLike.query.filter(
            PostLike.user_id ==self.id,
            PostLike.post_id == post.id).count() > 0

    #string to print out a row of column important in debugging
    def __repr__(self):
        return f"User {self.username}"



class Post(db.model):
    __table__ = "posts"


    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.Text)
    posted_at = db.Column(db.DateTime)
    upvotes = db.Column(db.Integer, default = 0)
    downvotes = db.Column(db.Integer, default = 0)
    post_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", 
                                    foreign_keys = "comment.post_id",
                                    backref = "post",
                                    lazy = "dynamic")
    

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_posts(cls,id):
        posts = Post.query.filter_by(user_id  = id).order_by(Post.posted_at.desc()).all()
        return posts

    @classmethod
    def get_all_posts(cls):
        return Post.query.order_by(Post.posted_at).all()
    @classmethod
    def get_all_posts(cls):
        return Post.query.order_by(Post.posted_at).all()


class Comment(db.Model):
    __tablename__ = "comments"


    id = db.column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_at = db.Column(db.DateTime)
    comment_by = db.Column(db.String)
    like_count = db.Column(db.Integer, default = 0)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comments(cls,id):
        gone = Comment.query.filter_by(id = id).first()
        db.session.delete(gone)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id = id).all()
        return comments



class Subscribers(db.Model):
    __table__ = "subscribers"
    id  = db.column(db.integer,primary_key = True)
    email = db.column(db.string(255), unique = True)


class PostLike(db.Model):
    __tablename__ = "post_like"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))


class Quote:
    """
    class qoutes consumed from the api endpoint
    """
    def __init__(self, author,quote):
        self.author = author
        self.quote = quote



    

      

       
