from basehandler import Handler
from google.appengine.ext import db
from models.comment import Comments
from models import post as pt

class EditCommentHandler(Handler):
    def get(self, post_id, comment_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=pt.blog_key())
            post = db.get(key)
            commented = Comments.get_by_id(comment_id)
            comment_message = commented.message
            if True:
                self.render('editcomment.html', action_comment = 'editcomment', action_comment_id = '/'+comment_id, user = self.user,  username = self.user, comment_message = comment_message, post = post)
            else:
                self.redirect('/login')
        else:
           self.redirect('/signup')

    def post(self, post_id, comment_id):
        message = self.request.get('message')
        Comments.editcommet(comment_id, message)
        self.redirect('/blog/%s' % post_id)
