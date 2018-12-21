import datetime
import threading

from general.flip_news_feed.utils.id_generator import IDGenerator


class CommentThread(object):
    comment_id_generator = IDGenerator(threading.Lock())

    def __init__(self):
        self.thread_id = self.comment_id_generator.generate_new_id()
        self.comment_time = datetime.datetime.utcnow()
        self._content = None
        self._user_id = None
        self._sub_comments = []

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    def readable_comment(self, offset):
        comment_str = " " * offset + "comment id: " + str(self.thread_id) + "\n"
        comment_str += " " * offset + str(self.user_id) + "\n"
        comment_str += " " * offset + self.content + "\n"
        comment_str += " " * offset + self.comment_time.isoformat() + "\n"

        # this piece is to print sub comments
        # for sub_comment in self._sub_comments:
        #     comment_str += self.readable_comment(offset + 5)
        return comment_str
