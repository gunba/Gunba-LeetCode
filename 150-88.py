class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []

        i1 = 0
        i2 = 0

        last_max = None

        def validate(arr, idx, max):
            if len(arr) > idx and isinstance(arr[idx], int):
                if not max or arr[idx] >= max:
                    return True
            return False
        
        def append(arr, elem, i):
            arr.append(elem)
            return i+1, elem

        # Iterate <total number of elements> times
        for x in range(m+n):
            # Validate the initial element in each array
            n1_val = validate(nums1, i1, last_max) and m-i1
            n2_val = validate(nums2, i2, last_max) and n-i2

            # Define element to avoid confusing indexes
            n1_elem = nums1[i1] if n1_val else None
            n2_elem = nums2[i2] if n2_val else None

            # If both values are valid, choose smallest
            if n1_val and n2_val:
                if n1_elem > n2_elem:
                    i2, last_max = append(temp, n2_elem, i2)
                else:
                    i1, last_max = append(temp, n1_elem, i1)
            # If only nums1 is valid, append value
            elif n1_val:
                i1, last_max = append(temp, n1_elem, i1)
            # If only nums2 is valid, append value
            elif n2_val:
                i2, last_max = append(temp, n2_elem, i2)
            # Neither side is valid. End.
            else:
                break
            
        # Replace nums1 with our new list.
        nums1[:] = temp

        print(temp)