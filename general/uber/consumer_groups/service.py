import random

from general.uber.consumer_groups.model import ConsumerGroup
from general.uber.consumer_groups.topic_consumer_groups.service import TopicConsumerGroupService


class ConsumerGroups(object):
    def __init__(self):
        self.consumer_groups = {}
        self.topic_consumer_group_service = TopicConsumerGroupService()

    def get_consumer_group(self, topic_name, cg_name):
        return self.consumer_groups[topic_name + "-" + cg_name]

    def add_consumer_group(self, topic_name, cg_name):
        consumer_group = ConsumerGroup()
        consumer_group.name = cg_name
        topic_consumer_group = self.topic_consumer_group_service.add_consumer_group(topic_name, cg_name)
        self.consumer_groups[topic_name + "-" + cg_name] = {}
        self.consumer_groups[topic_name + "-" + cg_name]["topic_consumer_group"] = topic_consumer_group
        self.consumer_groups[topic_name + "-" + cg_name]["consumer_group"] = consumer_group
        return consumer_group

    def add_consumer(self, topic_name, cg_name, consumer_obj):
        consumer_group = self.get_consumer_group(topic_name, cg_name)['consumer_group']
        consumer_group.consumers.append(consumer_obj)

    def process_message(self, topic_name, cg_name):
        consumer_group = self.get_consumer_group(topic_name, cg_name)['consumer_group']
        topic_consumer_group = self.get_consumer_group(topic_name, cg_name)['topic_consumer_group']
        consumer = random.choice(consumer_group.consumers)
        consumer.process_message(topic_consumer_group.offset.message_data)
        self.topic_consumer_group_service.move_offset(topic_consumer_group)