class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(1, len(s)):
            curr = s[i]
            j = i + 1
            while k > 0 or j < len(s) - 1:
                curr += s[j]
                if curr[0] != s[j]:
                    k -= 1
                j += 1
            res = max(len(curr), len(res))
            curr = s[i]
    
        return res
        