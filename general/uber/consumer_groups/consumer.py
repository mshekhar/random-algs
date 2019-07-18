import uuid


class BaseConsumer(object):
    def __init__(self):
        self.consumer_name = str(uuid.uuid4())

    def process_message(self, message):
        print self.consumer_name, message
