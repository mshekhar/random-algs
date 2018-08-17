from bisect import bisect_left


class Solution(object):
    def binary_search_find(self, a, x, lo=0, hi=None):
        hi = hi if hi is not None else len(a)
        pos = bisect_left(a, x, lo, hi)
        return pos

    def find_kth_ele_sorted_arrays(self, nums1, nums2, k):
        print nums1, nums2, k

        if not len(nums1) > 0:
            return nums2[k - 1]
        if not len(nums2) > 0:
            return nums1[k - 1]
        if k == len(nums1) + len(nums2):
            return max(nums1[-1], nums2[-1])
        if k == 0:
            return min(nums1[0], nums2[0])

        arr_1_mid = len(nums1) / 2
        arr_2_mid = len(nums2) / 2
        print arr_1_mid + arr_2_mid

        if arr_1_mid + arr_2_mid >= k:
            if nums1[arr_1_mid] > nums2[arr_2_mid]:
                nums1 = nums1[:arr_1_mid]
                return self.find_kth_ele_sorted_arrays(nums1, nums2, k)
            else:
                nums2 = nums2[:arr_2_mid]
                return self.find_kth_ele_sorted_arrays(nums1, nums2, k)
        else:
            if nums1[arr_1_mid] > nums2[arr_2_mid]:
                nums2 = nums2[arr_2_mid + 1:]
                return self.find_kth_ele_sorted_arrays(nums1, nums2, k - arr_2_mid - 1)
            else:
                nums1 = nums1[arr_1_mid + 1:]
                return self.find_kth_ele_sorted_arrays(nums1, nums2, k - arr_1_mid - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = (len(nums1) + len(nums2)) / 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (self.find_kth_ele_sorted_arrays(nums1, nums2, n) +
                    self.find_kth_ele_sorted_arrays(nums1, nums2, n - 1)) * 1.0 / 2
        else:
            return self.find_kth_ele_sorted_arrays(nums1, nums2, 1 + n)


# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], 3)
# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], 6)
# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], 7)
# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], 23)
# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], -1)
# print Solution().binary_search_find([1, 2, 6, 10, 18, 21], 99)
# import pdb
#
# pdb.set_trace()
# Solution().find_kth_ele_sorted_arrays([100, 112, 256], [72, 86, 113, 119, 265, 445, 892], 3)
def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    else:
        return sum(sorted(lst)[n // 2 - 1:n // 2 + 1]) / 2.0


nums1 = [100, 112, 256, 349, 770]
nums2 = [72, 86, 113, 119, 265, 445, 892]
nums3 = [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]

print median([1, 2, 3])
print Solution().findMedianSortedArrays([1, 3], [2])

# for i in [0, 3, 5, 7, 8, 2, 10]:
#     print 'starting for ', i
#     s = Solution().find_kth_ele_sorted_arrays(nums1, nums2, i)
#     print i, s, nums3[i]
