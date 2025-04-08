class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        window={}
        target={}
         
        for i in range(len(s1)):
            target[s1[i]]=1 + target.get(s1[i],0) 
        for i in range(len(s1)):
            window[s2[i]]=1 + window.get(s2[i],0)
            
        l=0
        for r in range(len(s1),len(s2)):
            if target==window:
                return True
        
            window[s2[r]]=1 + window.get(s2[r],0)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]  

            l+=1
        return target==window     


        