from basehandler import Handler
from models.post import Post

class BlogFront(Handler):
    #  A class that represent a RequestHandler for the main feed of the blog

    def get(self):
        if self.user:
          posts = Post.all().order('-created')
          self.render('frontPost.html', posts = posts, username = self.user)
        else:
          self.redirect('/login')
