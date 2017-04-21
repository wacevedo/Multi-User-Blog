import os
import webapp2
from handlers.basehandler import Handler
from handlers.signuphandler import SignUpHandler
from handlers.registerhandler import Register
from handlers.loginhandler import Login
from handlers.loginhandler import Logout
from handlers.blogfronthandler import BlogFront
from handlers.postpagehandler import PostPage
from handlers.newposthandler import NewPost
from handlers.editposthandler import EditPost
from handlers.welcomepagehandler import welcomepage
from handlers.likeposthandler import LikePost
from handlers.commenthandler import CommentHandler
from handlers.editcommenthandler import EditCommentHandler
from models.user import User

class MainPage(Handler):
    def get(self):
      self.redirect('/welcome')
      # self.response.headers['Content-Type'] = 'text/plain'
      # visits =  int(self.request.cookies.get('visits', 0))
      # visits += 1
      # self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)
      # self.write("You've been here %s times!" % visits)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)', PostPage),
    ('/likepost/([0-9]+)', LikePost),
    ('/editpost/([0-9]+)', EditPost),
    ('/editcomment/([0-9]+)/([0-9]+)', EditCommentHandler),
    ('/comment/([0-9]+)', CommentHandler),
    ('/blog/newpost', NewPost),
    ('/welcome', welcomepage)
], debug=True)
