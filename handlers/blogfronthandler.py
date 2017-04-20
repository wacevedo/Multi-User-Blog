from basehandler import Handler
from models.post import Post

class BlogFront(Handler):
    def get(self):
      posts = Post.all().order('-created') #select * from Post order by created desc limit 10
      self.render('frontPost.html', posts = posts) #here front.html
