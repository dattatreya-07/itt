class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10
        max_len = 0
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    current_len = len(str(val))
                    max_len = max(max_len, current_len)
                    break 
                val //= 10
        return max_len
