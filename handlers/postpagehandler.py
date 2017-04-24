from basehandler import Handler
from google.appengine.ext import db
from models.post import Post

class PostPage(Handler):
#  A class that represent a RequestHandler for get a single post

    def get(self, post_id):
        if self.user:
            post = Post.get_by_id(post_id)
            if not post:
                self.error(404)
                return
            self.render('permalink.html', action_comment = 'comment', post = post, user = self.user, username = self.user)
        else:
          self.redirect('/login')
