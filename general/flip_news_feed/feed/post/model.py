import datetime
import threading

from general.flip_news_feed.utils.id_generator import IDGenerator


class PostModel(object):
    post_id_generator = IDGenerator(threading.Lock())

    def __init__(self):
        self.post_id = self.post_id_generator.generate_new_id()
        self.content = None
        self.user_id = None

        self.post_time = datetime.datetime.utcnow()
        self.upvote_count = 0
        self.downvote_count = 0
        self.comment_count = 0

        # if self.freq == other.freq:
        #     return -1 * cmp(self.word, other.word)
        # return cmp(self.freq, other.freq)

    def readable_post(self):
        post_str = "post id: " + str(self.post_id) + "\n"
        post_str += str(self.upvote_count) + " upvotes, " + str(self.downvote_count) + " downvotes\n"
        post_str += str(self.user_id) + "\n"
        post_str += self.content + "\n"
        post_str += self.post_time.isoformat() + "\n"
        return post_str

    @property
    def upvote_score(self):
        return self.upvote_count - self.downvote_count
