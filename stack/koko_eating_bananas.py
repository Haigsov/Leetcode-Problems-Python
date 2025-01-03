import math


def minEatingSpeed(self, piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (r + l) // 2

        total_time = 0
        for p in piles:
            total_time += math.ceil(float(p) / k)
        if total_time <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res