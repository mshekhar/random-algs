from general.uber_in_memory_task_scheduler.beat import Beat
from general.uber_in_memory_task_scheduler.task.service import TaskService
from general.uber_in_memory_task_scheduler.thread_pool_executor import ThreadPoolExecutor


class TaskScheduler(object):
    def __init__(self, worker_count):
        self.task_service = TaskService()
        self.tpe = ThreadPoolExecutor(worker_count, self.task_service)
        self.beat = Beat(task_service=self.task_service, thread_pool_executor=self.tpe)
        self.total_tasks = 0

    def add_job(self, function, task_type, args, kwargs, task_interval_secs=0):
        if self.total_tasks == 0:
            self.beat.start()
            self.tpe.start()
        self.total_tasks += 1
        self.task_service.create_task(function, task_type, args, kwargs, task_interval_secs=task_interval_secs)


