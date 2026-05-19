class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        i = j = 0
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
