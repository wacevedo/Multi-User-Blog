import os
import webapp2
import jinja2
from helpers import salt
from models.user import User
import time

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
  t = jinja_env.get_template(template)
  return t.render(params)

def render_post(response, post):
  response.out.write('<b>'+ post.subject + '</b><br>')
  response.out.write(post.content)

class Handler(webapp2.RequestHandler): #here BlogHandler
    def write(self, *a, **kw):
      self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
      params['user'] = self.user
      t = jinja_env.get_template(template)
      return t.render(params)

    def render(self, template, **kw):
      self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
      cookie_val = salt.make_secure_val(val)
      self.response.headers.add_header('Set-Cookie', '%s=%s; Path/' % (name, cookie_val))

    def get_secure_cookie(self, name):
      cookie_val = self.request.cookies.get(name)
      return cookie_val and salt.check_secure_val(cookie_val)

    def login(self, user):
      self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
      self.response.headers.add_header('Set-Cookie', 'user_id=; Path/')

    def initialize(self, *a, **kw):
      webapp2.RequestHandler.initialize(self, *a, **kw)
      uid = self.get_secure_cookie('user_id')
      self.user = uid and User.by_id(int(uid))

    def redirect(self, s):
      time.sleep(0.3)
      super(Handler, self).redirect(s)
