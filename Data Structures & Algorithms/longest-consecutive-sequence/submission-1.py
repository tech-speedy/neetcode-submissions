class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0

        for i in nums:
            if i - 1 not in s:
                next_i = i + 1
                length = 1
                while next_i in s:
                    length += 1
                    next_i += 1
                result = max(result, length)

        return result