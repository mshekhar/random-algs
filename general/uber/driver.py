from general.uber.consumer_groups.consumer import BaseConsumer
from general.uber.consumer_groups.service import ConsumerGroups
from general.uber.topic.service import TopicService
# import pdb
# pdb.set_trace()
topic_service = TopicService()
topic = topic_service.create_topic("abc", 100)
topic_service.add_message(topic.name, message_obj="msg1")

consumer_group_service = ConsumerGroups()
cg1 = consumer_group_service.add_consumer_group(topic.name, "cg1")
cg2 = consumer_group_service.add_consumer_group(topic.name, "cg2")

consumer_group_service.add_consumer(topic.name, cg1.name, BaseConsumer())
consumer_group_service.add_consumer(topic.name, cg2.name, BaseConsumer())

consumer_group_service.process_message(topic.name, cg1.name)
consumer_group_service.process_message(topic.name, cg2.name)
