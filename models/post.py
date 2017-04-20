from handlers import basehandler
from google.appengine.ext import db
from models.user import User

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    user_id = db.IntegerProperty(required = True)
    user = db.ReferenceProperty(User, collection_name='posts')

    def render(self):
      self._render_text = self.content.replace('\n', '<br>')
      return basehandler.render_str('post.html', p = self)

    @classmethod
    def get_by_id(cls, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if post:
            return post
