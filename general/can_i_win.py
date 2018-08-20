import hashlib
import marshal


class Solution(object):
    def val_hash_func(self, x):
        return hashlib.md5(marshal.dumps(x)).hexdigest()

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        possible_vals = range(1, maxChoosableInteger + 1)
        if sum(possible_vals) < desiredTotal:
            return False
        return self.helper(possible_vals, desiredTotal, {})

    def helper(self, possible_vals, desiredTotal, hashed_vals):
        val_hash = self.val_hash_func(possible_vals)
        if val_hash in hashed_vals:
            return hashed_vals[val_hash]

        if possible_vals[-1] >= desiredTotal:
            return True

        for i in range(len(possible_vals)):
            if not self.helper(possible_vals[:i] + possible_vals[i + 1:], desiredTotal - possible_vals[i], hashed_vals):
                hashed_vals[val_hash] = True
                return True
        hashed_vals[val_hash] = False
        return False


print Solution().canIWin(10, 11)