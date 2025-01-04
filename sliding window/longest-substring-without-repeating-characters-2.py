def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) <= 0:
            return 0
        
        currentSubString = s[0]
        longestSubString = s[0]

        for i in range(1, len(s)):
            while s[i] in currentSubString:
                currentSubString = currentSubString[1:]
            
            else:
                currentSubString += s[i]
            
            if len(longestSubString) < len(currentSubString):
                longestSubString = currentSubString
        
        return len(longestSubString)