from basehandler import Handler


class welcomepage(Handler):
    #  A class that represent a RequestHandler for give the welcome to the user

    def get(self):
        if self.user:
            self.render('welcomepage.html', username=self.user)
        else:
            self.redirect('/signup')
