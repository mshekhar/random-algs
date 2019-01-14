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
        print op, ",", v
        res = getattr(news_feed_service, op)(*v)
        # print op, res
        # if op == "follow" and v == ["albus"]:
        #     print news_feed_service.user_service.get_following_users("tom")


print generic_runner([("signup", ["user_1"]),
                      ("signup", ["user_2"]),
                      ("signup", ["user_3"]),
                      ("login", ["user_3"]),
                      ("post", ["My first Post"]),
                      ("post", ["My second Post"]),
                      ("show_news_feed", []),
                      ("login", ["user_1"]),
                      ("upvote", [0]),
                      ("follow", ["user_3"]),
                      ("reply", [0, "welcome"]),
                      ("show_news_feed", []),
                      ("login", ["user_2"]),
                      ("post", ["Hello"]),
                      ("follow", ["user_2"]),
                      ("downvote", [0]),
                      ("downvote", [1]),
                      ("reply", [1, "Hi"]),
                      ("show_news_feed", [])
                      ])

# print generic_runner([("signup", ["lucious"]),
#                       ("signup", ["albus"]),
#                       ("signup", ["tom"]),
#                       ("login", ["tom"]),
#                       ("post", ["i am darkest all time"]),
#                       ("post", ["i am vold"]),
#                       ("show_news_feed", []),
#                       ("login", ["lucious"]),
#                       ("upvote", [0]),
#                       ("follow", ["tom"]),
#                       ("reply", [0, "i am with"]),
#                       ("show_news_feed", []),
#                       ("login", ["albus"]),
#                       ("post", ["happiness etc"]),
#                       ("follow", ["albus"]),
#                       ("downvote", [0]),
#                       ("downvote", [1]),
#                       ("reply", [1, "lol"]),
#                       ("show_news_feed", [])
#                       ])
