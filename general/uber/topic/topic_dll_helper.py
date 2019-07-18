from general.uber.topic.model import TopicMessage


class TopicDLLHelper(object):
    @classmethod
    def add_message(cls, topic, message_data, ttl):
        message = TopicMessage()
        message.message_data = message_data
        message.ttl = ttl
        if topic.dll_curr:
            topic.dll_curr.next = message
        else:
            topic.dll_curr = message
            topic.dll_head = message
        message.prev = topic.dll_curr
        topic.dll_curr = message
        return message

    @classmethod
    def delete_message(cls, dll_node):
        if dll_node.prev:
            dll_node.prev.next = dll_node.next
        if dll_node.next:
            dll_node.next.prev = dll_node.prev
