import Queue


class Solution(object):
    def swap(self, str_obj, idx_1, idx_2):
        new_str = str_obj[:]
        new_str[idx_1], new_str[idx_2] = new_str[idx_2], new_str[idx_1]
        return new_str

    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        A = list(A)
        B = list(B)
        if A == B:
            return 0
        visited = set()
        q = Queue.Queue()
        q.put(A)
        visited.add("".join(A))
        res = 0
        while q.qsize() > 0:
            size = q.qsize()
            i = 0
            while i < size:
                str_1 = q.get()
                if str_1 == B:
                    return res
                j = 0
                while j < len(str_1) and str_1[j] == B[j]:
                    j += 1
                k = j + 1
                while k < len(str_1):
                    if str_1[k] == B[j] and str_1[k] != B[k]:
                        new_str = self.swap(str_1, j, k)
                        hash_key = "".join(new_str)
                        if hash_key not in visited:
                            visited.add(hash_key)
                            q.put(new_str)
                    k += 1
                i += 1
            res += 1


print Solution().kSimilarity("ab", "ba")
print Solution().kSimilarity("abc", "bca")
print Solution().kSimilarity("abac", "baca")
print Solution().kSimilarity("aabc", "abca")
