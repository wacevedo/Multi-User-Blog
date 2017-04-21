from basehandler import Handler
from helpers import uservalidator as uv

class SignUpHandler(Handler):
    def get(self):
      self.render('signup.html')

    def post(self):
      have_error = False
      self.username = self.request.get('username')
      self.password = self.request.get('password')
      self.verify = self.request.get('verify')
      self.email = self.request.get('email')

      params = dict(username =  self.username, email = self.email)

      if not uv.valid_username(self.username):
        params['error_username'] = True
        have_error = True

      if not uv.valid_password(self.password):
        params['error_password'] = True
        have_error = True
      elif not uv.verify_password(self.password, self.verify):
        params['error_verify'] = True
        have_error = True

      if not uv.valid_email(self.email):
        params['error_email'] = True
        have_error = True

      if have_error:
        params['username'] = self.user
        self.render('signup.html', **params)
      else:
        self.done()

    def done(self, *a, **kw):
      raise NotImplementedError
