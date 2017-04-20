from basehandler import Handler
from models.like import Like
from models.post import Post

class LikePost(Handler):
    def get(self, post_id):
      if self.user and self.can_like(post_id):
        Like.like_it(self.user, post_id)
        self.redirect('/blog/' + str(post_id))
      else:
        self.redirect('/login')
        #you can like you own posts

    def can_like(self, pid):
      posttolike = Post.get_by_id(int(pid))
      userpost = posttolike.user.key().id_or_name()
      userloged = self.user.key().id_or_name()
      return userpost != userloged
