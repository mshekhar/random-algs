from collections import defaultdict


class CommentDao(object):
    def __init__(self):
        self.post_comments = defaultdict(list)
        self.comments = {}

    def add_comment(self, post_id, comment):
        self.comments[comment.thread_id] = comment
        self.post_comments[post_id].append(comment.thread_id)

    def get_post_comments(self, post_id):
        return map(lambda thread_id: self.get_comment_by_id(thread_id), self.post_comments[post_id])

    def get_post_comment_count(self, post_id):
        # raise post not found
        return len(self.post_comments[post_id])

    def get_comment_by_id(self, thread_id):
        # raise comment not found
        return self.comments[thread_id]

    def upvote_comment(self, comment_id):
        pass

    def downvote_comment(self, comment_id):
        pass
