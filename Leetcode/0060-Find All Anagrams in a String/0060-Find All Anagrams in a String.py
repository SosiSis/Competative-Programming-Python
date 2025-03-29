from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):return []
        target=Counter(p)
        window=Counter(s[:len(p)])

        res=[0] if target == window else []
        l=0
        for r in range(len(p),len(s)):
            window[s[r]]= 1+window.get(s[r],0)
            window[s[l]]-=1
            if window[s[l]]==0:
                window.pop(s[l])
            l +=1
            if window==target:    
                res.append(l)
                
         
        return res

        