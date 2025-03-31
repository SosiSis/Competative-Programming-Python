from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,total,res=0,0,0
        count=defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1
            while len(count)>2:
                count[fruits[l]]-=1
                total-=1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l+=1
            res=max(total,res)        


        return res