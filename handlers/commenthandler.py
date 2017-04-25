from basehandler import Handler
from models.comment import Comments


class CommentHandler(Handler):
    #  A class that represent a RequestHandler for create Comments

    def post(self, post_id):
        if self.user:
            message = self.request.get('message')
            if message:
                Comments.comment_it(self.user, post_id, message)
            self.redirect('/blog/%s' % post_id)
        else:
            self.redirect('/login')
