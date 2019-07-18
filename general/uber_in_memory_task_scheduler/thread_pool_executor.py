import threading
import time
from Queue import Queue

from general.uber_in_memory_task_scheduler.print_lock import print_sync_lock
from general.uber_in_memory_task_scheduler.task.model import TaskType


class TaskExecutor(threading.Thread):
    print_lock = threading.Lock()

    def __init__(self, task, task_service):
        self.task = task
        self.task_service = task_service
        self.is_completed = False
        super(TaskExecutor, self).__init__()

    def run(self):
        self.task.function(*self.task.args, **self.task.kwargs)
        self.task.last_run_time = time.time()
        if self.task.type == TaskType.CRON_MODIFIED:
            self.task.set_next_run_time()
            self.task_service.add_task_to_heap(self.task)
        with print_sync_lock:
            print time.time(), 'task exec launched ', self.task.function
        self.is_completed = True


class ThreadPoolExecutor(threading.Thread):
    def __init__(self, worker_count, task_service):
        self.task_queue = Queue()
        self.active_workers = {}
        self.task_counter = 0
        self.worker_count = worker_count
        self.task_service = task_service
        super(ThreadPoolExecutor, self).__init__()

    def clear_completed_tasks(self):
        tasks_to_remove = []
        for task_counter in self.active_workers:
            if self.active_workers[task_counter].is_completed:
                tasks_to_remove.append(task_counter)
        for task_counter in tasks_to_remove:
            self.active_workers.pop(task_counter)

    def add_task(self, task):
        self.task_queue.put(task)

    def run(self):
        while True:
            self.clear_completed_tasks()
            if self.task_queue.qsize() > 0:
                if len(self.active_workers) <= self.worker_count:
                    task = self.task_queue.get()
                    task_executor = TaskExecutor(task, self.task_service)
                    self.task_counter += 1
                    self.active_workers[self.task_counter] = task_executor
                    task_executor.start()
                else:
                    with print_sync_lock:
                        print time.time(), 'waiting for task completion with queue size ', self.task_queue.qsize()
                    time.sleep(5)
            else:
                with print_sync_lock:
                    print time.time(), 'waiting for new tasks'
                time.sleep(5)
