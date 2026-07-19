class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        for ch in s:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1
        for ch in t:
            if ch not in countt:
                countt[ch] = 1
            else:
                countt[ch] += 1
        
        if counts != countt:
            return False
        return True
            


        
        