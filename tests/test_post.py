import unittest
from app.models import post, User




class PostModelTest(unittest.TextCase):
    def setUp(self):
        self.user_amos = User(username='amos', password='kimu',email='kimutaiamos82@gmail.com')
        self.new_blogs = post(id=1,title='test',content='This is a test blog',user_id=self.user_kimutai.id)



        def tearDown(self):
            post.query.delete()
            User.query.delete()