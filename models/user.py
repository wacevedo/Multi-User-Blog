from google.appengine.ext import db
from helpers import salt

def users_key(group = 'default'):
  return db.Key.from_path('users', group)

class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
      return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
      return User.all().filter('name =', name).get()

    @classmethod
    def register(cls, name, pw, email = None):
      pw_hash = salt.make_pw_hash(name, pw)
      return User(parent = users_key(), name = name, pw_hash = pw_hash, email = email)

    @classmethod
    def login(cls, name, pw):
      u = cls.by_name(name)
      if u and salt.valid_pw(name, pw, u.pw_hash):
        return u
