class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) -1
        
        s1_count = {}
        window_count = {}

        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        for ch in range(len(s1)):
            window_count[s2[ch]] = window_count.get(s2[ch], 0) + 1

        if s1_count == window_count:
            return True

        while r < len(s2) -1:
            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            l += 1
            r += 1 
            
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            if s1_count == window_count:
                return True
        return False
            

            


