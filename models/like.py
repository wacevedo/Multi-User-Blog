from google.appengine.ext import db
from models.user import User
from models.post import Post


class Like(db.Model):
    post = db.ReferenceProperty(Post, collection_name='likes')
    user = db.ReferenceProperty(User, collection_name='likes')

    @classmethod
    def like_it(cls, uid, pid):
        posttolike = Post.get_by_id(int(pid))
        isliked = Like.all().filter('post =', posttolike).filter('user =', uid).get()
        if not isliked:
            postlike = Like(user=uid, post=posttolike)
            postlike.put()
        else:
            db.delete(isliked)
