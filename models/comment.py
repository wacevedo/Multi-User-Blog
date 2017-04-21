from google.appengine.ext import db
from models.user import User
from models.post import Post
from models import post as tools

class Comments(db.Model):
    post = db.ReferenceProperty(Post, collection_name='comments')
    user = db.ReferenceProperty(User, collection_name='comments')
    message = db.TextProperty(required = True)

    @classmethod
    def get_by_id(cls, comment_id):
        key = db.Key.from_path('Comments', int(comment_id))
        comment = db.get(key)
        if comment:
            return comment

    @classmethod
    def comment_it(cls, uid, pid, msg):
        posttocomment = Post.get_by_id(int(pid))
        commentofuser = Comments(user = uid, post = posttocomment, message = msg)
        commentofuser.put()

    @classmethod
    def delete_comment(cls, comment_id):
        comment = Comments.get_by_id(comment_id)
        db.delete(comment)

    @classmethod
    def editcommet(cls, comment_id, msg):
        comment = Comments.get_by_id(comment_id)
        comment.message = msg
        comment.put()
