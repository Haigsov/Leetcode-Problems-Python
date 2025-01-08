class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(0, len(s)):
            curr = s[i]
            j = i + 1
            while j < len(s):
                if curr[0] != s[j]:
                    if k > 0:
                        k -= 1
                    else:
                        break
                curr += s[j]
                j += 1
            res = max(len(curr), res)
    
        return res