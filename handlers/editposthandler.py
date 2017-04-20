from basehandler import Handler
from google.appengine.ext import db
from models import post as pt

class EditPost(Handler):
    def get(self, post_id):
      if self.user:
        key = db.Key.from_path('Post', int(post_id), parent=pt.blog_key())
        post = db.get(key)
        if post.user_id == self.user.key().id_or_name():
          self.render('newpost.html', task = 'Edit', subject= post.subject, content= post.content)
        else:
          self.redirect('/login')
      else:
        self.redirect('/signup')

    def post(self, post_id):
      subject = self.request.get('subject')
      content = self.request.get('content')

      if subject and content and self.user:
        key = db.Key.from_path('Post', int(post_id), parent=pt.blog_key())
        post = db.get(key)
        post.subject = subject
        post.content = content
        post.put()
        self.redirect('/blog/%s' % str(post_id))
      else:
        error = 'subject and content please!'
        self.render('newpost.html', task = 'New', subject= subject, content= content, error= error)

