from basehandler import Handler
from models import post as pt


class NewPost(Handler):
    #  A class that represent a RequestHandler for create new posts

    def get(self):
        if self.user:
            self.render("newpost.html", task='New', username=self.user)
        else:
            self.redirect('/login')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content and self.user:
            p = pt.Post(parent=pt.blog_key(), subject=subject,
                        content=content, user_id=self.user.key().id_or_name(),
                        user=self.user)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = 'subject and content please!'
            self.render('newpost.html', task='New', subject=subject,
                        username=self.user, content=content, error=error)
