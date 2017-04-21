from basehandler import Handler
from models.comment import Comments

class DeleteCommentHandler(Handler):
    def get(self, post_id, comment_id):
        if self.user:
            Comments.delete_comment(comment_id)
            self.redirect('/blog/%s' % post_id)
        else:
            self.redirect('/login')
