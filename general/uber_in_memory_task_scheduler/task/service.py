import heapq
import threading
import time

from general.uber_in_memory_task_scheduler.task.model import Task, TaskType


class TaskService(object):
    def __init__(self):
        self.tasks = {}
        self.tasks_heap = []
        self.lock = threading.Lock()

    def create_task(self, function, task_type, args, kwargs, task_interval_secs=0):
        with self.lock:
            task = Task()
            task.function = function
            task.args = args
            task.kwargs = kwargs
            task.type = task_type
            task.task_interval_secs = task_interval_secs
            task.next_run_time = time.time() + task.task_interval_secs
            self.tasks[task.task_id] = task
            self.add_task_to_heap(task)

    def delete_task(self, task_id):
        self.tasks.pop(task_id, None)

    def add_task_to_heap(self, task):
        heapq.heappush(self.tasks_heap, (task.next_run_time, task))

    def get_expired_tasks(self, expiration_time):
        with self.lock:
            expired_tasks = []
            while self.tasks_heap and self.tasks_heap[0][0] < expiration_time:
                task = heapq.heappop(self.tasks_heap)[1]
                if task.type == TaskType.CRON:
                    task.set_next_run_time()
                    self.add_task_to_heap(task)
                expired_tasks.append(task)
        return expired_tasks
