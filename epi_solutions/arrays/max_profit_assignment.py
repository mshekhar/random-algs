class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        worker.sort()
        profit = 0
        job_idx = 0
        max_profit = 0
        for i in worker:
            # print i, jobs[job_idx][0], max_profit
            while len(jobs) > job_idx and i >= jobs[job_idx][0]:
                # print 'inc ', max_profit, jobs[job_idx][1], max(max_profit, jobs[job_idx][1])
                max_profit = max(max_profit, jobs[job_idx][1])
                job_idx += 1
            # print max_profit, job_idx
            profit += max_profit

        return profit


print Solution().maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7])
