class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for ch in range(len(nums)):
            if nums[ch] == target:
                return ch
        return -1
        