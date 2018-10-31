class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        total_tasks = len(tasks)
        completed_tasks = 0
        remaining_tasks = total_tasks
        task_counter = [0] * 26
        for task in tasks:
            task_counter[ord(task) - ord('A')] += 1
        next_run_time = [-1] * 26

        t = 0
        while remaining_tasks:
            max_task_index = None
            most_frequent_task = 0
            for c, i in enumerate(task_counter):
                if i > 0 and next_run_time[c] < t and i > most_frequent_task:
                    max_task_index = c
                    most_frequent_task = i
            if max_task_index is None:
                t += 1
                continue
            task_counter[max_task_index] -= 1
            next_run_time[max_task_index] = t + n
            # print most_frequent_task, max_task_index, task_counter, next_run_time
            remaining_tasks -= 1
            completed_tasks += 1
            t += 1
        return t


print Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2)
print Solution().leastInterval(["A"], 2)
print Solution().leastInterval(["A", "B", "A"], 2)
print Solution().leastInterval(["A", "B", "A"], 1)
print Solution().leastInterval([], 1)
