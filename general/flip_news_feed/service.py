from general.flip_news_feed.account.user.service import UserService
from general.flip_news_feed.feed.comments.service import CommentService
from general.flip_news_feed.feed.post.service import PostService


class NewsFeedService(object):
    active_user = None

    def __init__(self):
        self.user_service = UserService()
        self.comment_service = CommentService()
        self.post_service = PostService()

    def post(self, content):
        self.post_service.create_new_post(user_id=self.active_user, content=content)

    def follow(self, user_id_2):
        self.user_service.follow_user(user_id_1=self.active_user, user_id_2=user_id_2)

    def reply(self, post_id, content):
        self.comment_service.create_new_comment(post_id=post_id, content=content, user_id=self.active_user)
        self.post_service.add_comment(post_id)

    def upvote(self, post_id):
        self.post_service.upvote_post(post_id)

    def downvote(self, post_id):
        self.post_service.downvote_post(post_id)

    def signup(self, name):
        return self.user_service.create_new_user(name=name)

    def login(self, name):
        self.user_service.login_user(name, "**")
        self.active_user = name

    def _post_comparator(self, user_id):
        following_users = self.user_service.get_following_users(user_id)

        def compare(post_1, post_2):
            if int(post_1.user_id in following_users) == int(post_2.user_id in following_users):
                if post_1.upvote_count - post_1.downvote_count == post_2.upvote_count - post_2.downvote_count:
                    if post_1.comment_count == post_2.comment_count:
                        return cmp(post_1.post_time, post_2.post_time)
                    return cmp(post_1.comment_count, post_2.comment_count)
                return cmp(post_1.upvote_count - post_1.downvote_count, post_2.upvote_count - post_2.downvote_count)
            return cmp(int(post_1.user_id in following_users), int(post_2.user_id in following_users))

        return compare

    def show_news_feed(self):
        sorted_posts = sorted(self.post_service.get_all_posts(),
                              cmp=self._post_comparator(self.active_user),
                              reverse=True)

        for post in sorted_posts:
            print post.readable_post()
            for comment in self.comment_service.get_comments_for_post(post.post_id):
                print comment.readable_comment(offset=5)
