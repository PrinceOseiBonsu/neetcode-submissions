class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = sorted(s1)
        r = len(s1)

        for i in range(len(s2)- r + 1):
            window = s2[i:i +r]

            if sorted(window) == s1:
                return True
        return False