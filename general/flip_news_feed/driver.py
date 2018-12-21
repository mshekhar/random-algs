# import sys
# from os import path
#
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
# print path.dirname(path.dirname(path.abspath(__file__)))
from general.flip_news_feed.service import NewsFeedService


def generic_runner(oper_args_list):
    news_feed_service = NewsFeedService()
    c = 1
    for op, v in oper_args_list:
        res = getattr(news_feed_service, op)(*v)
        print op, res
        if op == "follow" and v == ["albus"]:
            print news_feed_service.user_service.get_following_users("tom")


print generic_runner([("signup", ["lucious"]),
                      ("signup", ["albus"]),
                      ("signup", ["tom"]),
                      ("login", ["tom"]),
                      ("post", ["i am darkest all time"]),
                      ("post", ["i am vold"]),
                      ("show_news_feed", []),
                      ("login", ["lucious"]),
                      ("upvote", [0]),
                      ("follow", ["tom"]),
                      ("reply", [0, "i am with"]),
                      ("show_news_feed", []),
                      ("login", ["albus"]),
                      ("post", ["happiness etc"]),
                      ("follow", ["albus"]),
                      ("downvote", [0]),
                      ("downvote", [1]),
                      ("reply", [1, "lol"]),
                      ("show_news_feed", [])
                      ])
