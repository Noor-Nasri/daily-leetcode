class Solution:
    # This question is honestly just a long torture. 
    # Why not just do it in O(n+m) and call it a day? Way more readable
    # There is a +-1 bug somewhere in this code and I am too tired
    # If you see this, I am sorry for letting you down 
    # - this "hard" is more annoying than hard. But I can solve it on paper.

    # So, I did the O(n+m) at the end. Enjoy.

    '''
    def getMedian(self, nums, st, en):
        midway = (st + en - 1) // 2
        if (en - st) % 2: return nums[midway]
        return (nums[midway] + nums[midway + 1])/2

    def solveKth(self, nums1, nums2, st1, en1, st2, en2, k):
        print("Got call: ", st1, en1, st2, en2, k)
        # Returns (arr, ind in arr) of kth index value in  nums1[st1, en1) (+) other
        if st1 >= en1: return (2, st2 + k)
        elif st2 >= en2: return (1, st1 + k)
        
        med1 = self.getMedian(nums1, st1, en1)
        med2 = self.getMedian(nums2, st2, en2)
        numElements = en1 - st1 + en2 - st2
        print("Found out ", med1, med2, numElements)

        # All Elements at cutoff+ are >= their arr median
        cutoff1 = (en1 + st1 - 1)//2
        if (en1 - st1) % 2 == 0: cutoff1+= 1
        cutoff2 = (en2 + st2 - 1)//2
        if (en2 - st2) % 2 == 0: cutoff2+= 1


        # At cutoff1+, >= elements before cutoff1 and elements before cutoff2
        sizeSection = en1 + en2 - cutoff1 - cutoff2
        print("Section size is", sizeSection)

        if med1 >= med2:
            # Top half of list1 are ALL >= first half of both lists.
            # Ie. Top half of list1 are in top 50% of elements
            # and bottom half of list2 are in bottom 50% of elements
            # Based on where k is, we can remove half of l1 or half of l2

            if k <= numElements - sizeSection:
                # We want to go into the section WITHOUT nums1[cutoff1:]
                print("Isolating top half nums1")
                return self.solveKth(nums1, nums2,  st1, cutoff1, st2, en2, k)
            else:
                # We want to go beyond s1, bums2[:c2] are all in s1
                print("Isolating bottom half nums2[:cutoff2]")
                return self.solveKth(nums1, nums2,  st1, en1, cutoff2, en2, k - (cutoff2 - en2))
        
        else:
            # Symmetric logic
            if k <= numElements - sizeSection:
                # We want to go into the section WITHOUT nums1[cutoff1:]
                print("Isolating top half nums2")
                return self.solveKth(nums1, nums2,  st1, en1, st2, cutoff2, k)
            else:
                # We want to go beyond s1, bums2[:c2] are all in s1
                print("Isolating bottom half nums1[:cutoff1]")
                return self.solveKth(nums1, nums2,  cutoff1, en1, st2, en2, k - (cutoff1 - en2)) 


        return

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0: return self.getMedian(nums2, 0, len(nums2))
        if len(nums2) == 0: return self.getMedian(nums1, 0, len(nums1))

        ind_arr, ind_element =  self.solveKth(nums1, nums2, 0, len(nums1), 0, len(nums2), 
            (len(nums1) + len(nums2) - 1) // 2)
        
        # If even total, need to find element strictly bigger (just binary search)
        print("=====")
        print("Recieved", ind_arr, ind_element)
        arr = (ind_arr == 1 and nums1 or nums2)
        """ target = arr[ind_element]
        if (len(nums1) + len(nums2)) % 2:
            return target

        # Do binary search to find next element in other nums
        possible_next = []
        if len(arr) > ind_element + 1:
            possible_next.append(arr[ind_element + 1])

        second_arr = (ind_arr == 1 and nums2 or nums1)
        low = 0
        high = len(second_arr) - 1
        mid = 0 # need to remember last mid

        while low <= high:
            mid = (low + high) // 2
            if second_arr[mid] == target: return target
            elif second_arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if second_arr[mid] > target:
            possible_next.append(second_arr[mid]) # Pointer on the > cutoff
        elif len(second_arr) > mid - 1:
            possible_next.append(second_arr[mid + 1]) # Pointer on the < cutoff
        
        return (target + min(possible_next)) / 2
        """


        '''


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cur = []
        ind1 = 0
        ind2 = 0
        target = (len(nums1) + len(nums2)) // 2 + 1

        while True:
            if ind1 >= len(nums1) or (ind2 < len(nums2) and nums2[ind2] < nums1[ind1]):
                cur.append(nums2[ind2])
                ind2 += 1
            else:
                cur.append(nums1[ind1])
                ind1 += 1
            
            if len(cur) == target:
                if (len(nums1) + len(nums2)) % 2:
                    return cur[-1]
                else:
                    return (cur[-1] + cur[-2])/2

        return 0

        
        

        