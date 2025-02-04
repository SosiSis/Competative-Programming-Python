class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping={ "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        newInteger=0
        n=len(s)
        for i in range(n):
            current_val= mapping[s[i]]
            if i < n-1 and current_val < mapping[s[i+1]]:
                newInteger-= current_val
            else:
                newInteger+= current_val
        return newInteger



sol=Solution()
print(sol.romanToInt("III"))



        