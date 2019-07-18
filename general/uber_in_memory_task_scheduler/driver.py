import time

from general.uber_in_memory_task_scheduler.task.model import TaskType
from general.uber_in_memory_task_scheduler.task_scheduler import TaskScheduler

task_scheduler = TaskScheduler(3)


def func_1(a, b=3):
    # print ' func_1', a, b
    time.sleep(6)


task_scheduler.add_job(function=func_1, args=(1,), kwargs={'b': 5}, task_type=TaskType.ONCE)
task_scheduler.add_job(function=func_1, args=(1,), kwargs={'b': 5}, task_type=TaskType.CRON, task_interval_secs=10)
task_scheduler.add_job(function=func_1, args=(1,), kwargs={'b': 5}, task_type=TaskType.CRON_MODIFIED,
                       task_interval_secs=10)
task_scheduler.add_job(function=func_1, args=(1,), kwargs={'b': 5}, task_type=TaskType.CRON, task_interval_secs=10)
task_scheduler.add_job(function=func_1, args=(1,), kwargs={'b': 5}, task_type=TaskType.CRON, task_interval_secs=10)

