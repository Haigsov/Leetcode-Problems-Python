def lengthOfLongestSubstring(self, s):
    """"
    :type s: str
    :rtype: int
    """

    char_set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    
    return res
    """
    old solution
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
        
    
    return len(res)"""