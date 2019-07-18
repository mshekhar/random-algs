import heapq
import threading
import time

from general.uber.topic.model import Topic
from general.uber.topic.topic_dll_helper import TopicDLLHelper


class TopicService(object):
    topics = {}

    def create_topic(self, topic_name, ttl=60 * 60 * 60):
        topic = Topic()
        topic.name = topic_name
        topic.default_ttl = ttl
        self.topics[topic_name] = topic
        return topic

    @classmethod
    def get_topic(cls, topic_name):
        topic = cls.topics.get(topic_name)
        if not topic:
            raise Exception('invalid topic')
        return topic

    def delete_topic(self):
        pass

    def add_message(self, topic_name, message_obj, ttl=None):
        # topic = Topic()
        topic = self.get_topic(topic_name)
        if not ttl:
            ttl = topic.default_ttl

        message = TopicDLLHelper.add_message(topic, message_obj, ttl)
        heapq.heappush(topic.offset_min_heap, (int(time.time()) + ttl, message))
