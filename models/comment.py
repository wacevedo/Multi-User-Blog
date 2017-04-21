from google.appengine.ext import db
from models.user import User
from models.post import Post

class Comments(db.Model):
    post = db.ReferenceProperty(Post, collection_name='comments')
    user = db.ReferenceProperty(User, collection_name='comments')
    message = db.TextProperty(required = True)

    @classmethod
    def comment_it(cls, uid, pid, msg):
        posttolike = Post.get_by_id(int(pid))
        # isliked = Comments.all().filter('post =', posttolike).filter('user =', uid).get()
        postlike = Comments(user = uid, post = posttolike, message = msg)
        postlike.put()

    def delete_comment(cls, comm):
        return None
        # db.delete(comm)