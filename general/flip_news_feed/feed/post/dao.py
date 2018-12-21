class PostDao(object):
    def __init__(self):
        self.posts = {}

    def add_post(self, post_id, post):
        self.posts[post_id] = post

    def get_post(self, post_id):
        # raise post not found
        return self.posts[post_id]

    def upvote_post(self, post_id):
        # raise post not found
        self.posts[post_id].upvote_count += 1

    def downvote_post(self, post_id):
        # raise post not found
        self.posts[post_id].downvote_count += 1

    def increment_comment_count(self, post_id):
        # raise post not found
        self.posts[post_id].comment_count += 1
