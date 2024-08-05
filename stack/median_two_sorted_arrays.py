def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
            
        total = len(nums1) + len(nums2)
        half  = total // 2

        if len(nums2) > len(nums1):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-infinity")
            if (i + 1) < len(A):
                Aright = A[i + 1]
            else:
                Aright = float("infinity")

            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float("-infinity")

            if (j + 1) < len(B):
                Bright = B[j + 1]
            else:
                Bright = float("infinity")
            
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
