import threading
import time

from general.uber_in_memory_task_scheduler.print_lock import print_sync_lock


class Beat(threading.Thread):
    def __init__(self, task_service, thread_pool_executor, beat_interval=5):
        self.task_service = task_service
        self.beat_interval = beat_interval
        self.thread_pool_executor = thread_pool_executor
        super(Beat, self).__init__()

    def run(self):
        while True:
            expired_tasks = self.task_service.get_expired_tasks(time.time())
            for task in expired_tasks:
                # put task to TPE queue
                self.thread_pool_executor.add_task(task)
            with print_sync_lock:
                print time.time(), Beat.__class__.__name__, 'pushed ', len(expired_tasks), ' to queue sleeping for ', self.beat_interval
            time.sleep(self.beat_interval)
