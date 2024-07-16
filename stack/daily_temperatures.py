def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    
    res = [0] * len(temperatures)
    s = []
    
    for i, t in enumerate(temperatures):
        while s and t > s[-1][0]:
            stackT, stackInd = s.pop()
            res[stackInd] = i - stackInd
        s.append((t, i))
    
    return res