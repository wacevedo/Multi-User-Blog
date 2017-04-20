from basehandler import Handler
from google.appengine.ext import db
from models.post import Post

class PostPage(Handler):
    def get(self, post_id):
      post = Post.get_by_id(post_id)

      if not post:
        self.error(404)
        return

      self.render('permalink.html', post = post, user = self.user, username = self.user)
