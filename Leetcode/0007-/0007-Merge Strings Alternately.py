class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        if len(word1) > 0 or len(word2) > 0:
            mergedString=""
            for ch1, ch2 in zip(word1, word2):
                mergedString+=ch1 + ch2

            mergedString += word1[len(word2):] + word2[len(word1):]   
            return mergedString 
          
    
sol= Solution()
print(sol.mergeAlternately("abc","def"))