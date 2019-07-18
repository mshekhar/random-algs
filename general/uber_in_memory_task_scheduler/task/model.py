import time
import uuid


class TaskType(object):
    CRON = 1
    CRON_MODIFIED = 2
    ONCE = 3


class Task(object):
    def __init__(self):
        self.function = None
        self.task_id = uuid.uuid4()
        self.args = []
        self.kwargs = {}
        self.next_run_time = None
        self.last_run_time = None
        self.task_interval_secs = 0
        self.type = None

    def set_next_run_time(self):
        if self.type == TaskType.CRON_MODIFIED:
            self.next_run_time = self.last_run_time + self.task_interval_secs
        elif self.type == TaskType.CRON:
            self.next_run_time = time.time() + self.task_interval_secs
