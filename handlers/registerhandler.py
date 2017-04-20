from signuphandler import SignUpHandler
from models.user import User

class Register(SignUpHandler):
    def done(self):
      u = User.by_name(self.username)
      if u:
        msg = 'That user already exists.'
        self.render('signup.html', error_username_msg = msg)
      else:
        u = User.register(self.username, self.password, self.email)
        u.put()

        self.login(u)
        self.redirect('/welcome')