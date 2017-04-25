from basehandler import Handler
from google.appengine.ext import db
from models import post as pt


class EditPost(Handler):
    #  A class that represent a RequestHandler for edit post

    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=pt.blog_key())
            post = db.get(key)
            if post.user.key().id_or_name() == self.user.key().id_or_name():
                self.render('newpost.html', task='Edit', post=post,
                            username=self.user, subject=post.subject,
                            content=post.content)
            else:
                self.redirect('/login')
        else:
            self.redirect('/signup')

    def post(self, post_id):
        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')
            if subject and content and self.user:
                key = db.Key.from_path('Post', int(post_id),
                                       parent=pt.blog_key())
                post = db.get(key)
                if post.user.key().id_or_name() == self.user.key().id_or_name():
                    post.subject = subject
                    post.content = content
                    post.put()
                    self.redirect('/blog/%s' % str(post_id))
                else:
                    self.redirect('/login')
            else:
                error = 'subject and content please!'
                self.render('newpost.html', task='New', username=self.user,
                            subject=subject, content=content, error=error)
        else:
            self.redirect('/signup')
