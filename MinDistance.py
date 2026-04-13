class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                min_dist = min(min_dist, abs(i - start))
        return min_dist
