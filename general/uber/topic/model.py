class TopicMessage(object):
    def __init__(self):
        self.ttl = None
        self.message_data = None
        self.next = None
        self.prev = None


class Topic(object):
    def __init__(self):
        self.name = None
        self.default_ttl = None
        self.offset_min_heap = []
        self.dll_head = None
        self.dll_curr = None
        self.total_messages = 0
