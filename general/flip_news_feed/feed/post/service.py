from general.flip_news_feed.account.user.service import UserService
from general.flip_news_feed.feed.comments.service import CommentService
from general.flip_news_feed.feed.post.dao import PostDao
from general.flip_news_feed.feed.post.model import PostModel


class PostService(object):
    def __init__(self):
        self.post_model = PostModel
        self.post_dao = PostDao()
        self.comment_service = CommentService()
        self.user_service = UserService()

    def create_new_post(self, **creation_kwargs):
        new_post = self.post_model()
        new_post.content = creation_kwargs.pop("content")
        new_post.user_id = creation_kwargs.pop("user_id")
        self.post_dao.add_post(new_post.post_id, new_post)

    def add_comment(self, post_id):
        self.post_dao.increment_comment_count(post_id)

    def upvote_post(self, post_id):
        self.post_dao.upvote_post(post_id)

    def downvote_post(self, post_id):
        self.post_dao.downvote_post(post_id)

    def get_all_posts(self):
        return self.post_dao.posts.values()
