from basehandler import Handler
from models.comment import Comments

class DeleteCommentHandler(Handler):
#  A class that represent a RequestHandler for delete Comments

    def get(self, post_id, comment_id):
        if self.user:
            commented = Comments.get_by_id(comment_id)
            if Comments.can_comment(commented, self.user):
                Comments.delete_comment(comment_id, self.user)
            self.redirect('/blog/%s' % post_id)
        else:
            self.redirect('/login')
