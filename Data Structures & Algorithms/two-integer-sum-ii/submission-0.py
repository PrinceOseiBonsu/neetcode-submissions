class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new = []
        left = 0
        right = len(numbers)- 1

        while left < right:
            new = numbers[left] + numbers[right] 

            if new > target:
                right -= 1

            elif new < target:
                left +=1
            else:
                return [ left + 1, right + 1]
        