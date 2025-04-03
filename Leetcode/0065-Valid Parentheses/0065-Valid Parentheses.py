class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in mydict.keys():
                stack.append(char)  
            else:
                if not stack or mydict[stack.pop()] != char:  
                    return False
        
        return stack==[]
