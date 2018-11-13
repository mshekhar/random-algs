class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0:
            return "0"
        res = ["-" if (numerator > 0) ^ (denominator > 0) else ""]
        denominator = abs(denominator)
        numerator = abs(numerator)
        res.append(str(numerator / denominator))

        numerator %= denominator
        if numerator == 0:
            return "".join(res)
        res.append(".")
        num_map = dict()
        num_map[numerator] = len(res)
        while numerator != 0:
            numerator *= 10
            res.append(str(numerator / denominator))
            # print numerator, denominator, num_map, res
            numerator %= denominator
            if numerator in num_map:
                idx = num_map[numerator]
                res.insert(idx, "(")
                res.append(")")
                break
            else:
                num_map[numerator] = len(res)
        return "".join(res)


print Solution().fractionToDecimal(1, 7)
