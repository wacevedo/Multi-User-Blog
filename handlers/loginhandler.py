from basehandler import Handler
from models.user import User

class Login(Handler):
    def get(self):
      self.render('login.html')

    def post(self):
      username = self.request.get('username')
      password = self.request.get('password')

      u = User.login(username, password)
      if u:
        self.login(u)
        self.redirect('/welcome')
      else:
        msg = 'Invalid login'
        self.render('login.html', error = msg)

class Logout(Handler):
    def get(self):
      self.logout()
      self.redirect('/signup')