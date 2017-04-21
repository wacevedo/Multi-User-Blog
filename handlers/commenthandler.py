from basehandler import Handler
from models.comment import Comments

class CommentHandler(Handler):
    def post(self, post_id):
      message = self.request.get('message')
      Comments.comment_it(self.user, post_id, message)
      self.redirect('/blog/%s' % post_id)
