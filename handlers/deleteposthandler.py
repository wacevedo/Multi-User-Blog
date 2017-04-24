from basehandler import Handler
from models.post import Post

class DeletePostHandler(Handler):
    def get(self, post_id):
        if self.user:
            p = Post.get_by_id(post_id)
            if p.user.key().id() == self.user.key().id():
                Post.delete_post(p)
            self.redirect('/blog')
        else:
            self.redirect('/login')
