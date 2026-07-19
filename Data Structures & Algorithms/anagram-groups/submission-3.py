class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        new = []

        for word in strs:
            key = tuple(sorted(word))
            if key not in seen:
                seen[key] = []
            
            seen[key].append(word)
        
        return list(seen.values())
