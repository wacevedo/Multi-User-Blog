from basehandler import Handler

class LikePost(Handler):
    def get(self, post_id):
      user = self.request.get('username')
      if self.user:
        # check if user already like this post
        self.render('welcomepage.html', username = self.user.name)
      else:
        #error message like

