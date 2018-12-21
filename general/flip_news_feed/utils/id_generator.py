class IDGenerator(object):
    curr_id = -1

    def __init__(self, lock):
        self.lock = lock

    def generate_new_id(self):
        with self.lock:
            self.curr_id += 1
        return self.curr_id

