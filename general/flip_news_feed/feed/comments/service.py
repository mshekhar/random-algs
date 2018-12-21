from general.flip_news_feed.feed.comments.dao import CommentDao
from general.flip_news_feed.feed.comments.model import CommentThread


class CommentService(object):
    def __init__(self):
        self.comment_model = CommentThread
        self.comment_dao = CommentDao()

    def create_new_comment(self, post_id, **creation_kwargs):
        new_comment = self.comment_model()
        new_comment.content = creation_kwargs.pop("content")
        new_comment.user_id = creation_kwargs.pop("user_id")
        self.comment_dao.add_comment(post_id, new_comment)

    def get_comments_for_post(self, post_id):
        return self.comment_dao.get_post_comments(post_id)

    def get_comment_by_thread_id(self, thread_id):
        return self.comment_dao.get_comment_by_id(thread_id)

    def get_comment_count_for_post(self, post_id):
        return self.comment_dao.get_post_comment_count(post_id)
