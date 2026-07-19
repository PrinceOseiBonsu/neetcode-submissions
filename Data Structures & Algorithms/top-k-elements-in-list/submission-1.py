class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for ch in nums:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] =  1


        sorted_items = sorted(count.items(), key= lambda x:x[1], reverse = True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])
        return result

        