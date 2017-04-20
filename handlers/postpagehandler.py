from basehandler import Handler
from google.appengine.ext import db
from models import post as pt
from models import user as us

class PostPage(Handler):
    def get(self, post_id):
      key = db.Key.from_path('Post', int(post_id), parent=pt.blog_key())
      post = db.get(key)

      if not post:
        self.error(404)
        return

      user = us.User.get_by_id(post.user_id, parent = us.users_key())

      self.render('permalink.html', post = post, name = user.name)
