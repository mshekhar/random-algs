import collections

from general.uber.consumer_groups.topic_consumer_groups.model import TopicConsumerGroup
from general.uber.topic.service import TopicService


class TopicConsumerGroupService(object):
    def __init__(self):
        self.consumer_groups_by_topic = collections.defaultdict(list)

    def add_consumer_group(self, topic_name, consumer_group):
        topic_consumer_group = TopicConsumerGroup()
        topic_consumer_group.topic = TopicService.get_topic(topic_name)
        topic_consumer_group.consumer_group = consumer_group
        topic_consumer_group.offset = topic_consumer_group.topic.dll_head
        self.consumer_groups_by_topic[topic_name].append(consumer_group)
        return topic_consumer_group

    def move_offset(self, topic_consumer_group):
        topic_consumer_group.offset = topic_consumer_group.offset.next
