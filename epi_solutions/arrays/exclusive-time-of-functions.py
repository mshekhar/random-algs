class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0] * n
        prev_time = 0
        for log in logs:
            log_split = log.split(":")
            func_id, oper, timestamp = int(log_split[0]), log_split[1], int(log_split[2])
            if oper == "start":
                if stack:
                    res[stack[-1][0]] += timestamp - prev_time
                stack.append((func_id, oper, timestamp))
                prev_time = timestamp
            else:
                # print stack, log_split
                res[stack.pop()[0]] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res


print Solution().exclusiveTime(n=2, logs=["0:start:0",
                                          "1:start:2",
                                          "1:end:5",
                                          "0:end:6"])
