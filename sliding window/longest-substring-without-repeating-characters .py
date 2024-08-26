def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    res = ""
    seq = ""

    for st in s:
        if st in seq:
            seq = st
        else:
            seq += st
        res = max(res, seq, key=len)
    
    for i in range(len(s) - 1, 0, -1):
        if s[i] in seq:
            seq = s[i]
        else:
            seq += s[i]
        res = max(res, seq, key=len)
        
    
    return len(res)