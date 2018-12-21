import threading
from abc import ABCMeta

from general.flip_news_feed.utils.id_generator import IDGenerator


class Account(object):
    __metaclass__ = ABCMeta
    account_id_generator = IDGenerator(threading.Lock())

    def __init__(self):
        self.account_id = self.account_id_generator.generate_new_id()
        self._password = None
