class DDPost:

    def __init__(self, post):
        self.post = post
        self.get_post_info()


    def get_post_info(self):
        self.body = self.post.selftext
        self.itle = self.post.title
        self.author = self.post.author
        self.id = self.post.id

        
