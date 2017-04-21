from basehandler import Handler

class welcomepage(Handler):
    def get(self):
      if self.user:
        self.render('welcomepage.html', username = self.user)
      else:
        self.redirect('/signup')
