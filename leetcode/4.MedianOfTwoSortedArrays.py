class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)+len(nums2)
        poped_item_counter = 0
        if n%2 == 1:
            median_nr = n//2 + 1
            if len(nums1) == 0:
                return float(nums2[median_nr-1])
            elif len(nums2) == 0:
                return float(nums1[median_nr-1])
            else:
                while poped_item_counter < median_nr-1:
                    if len(nums1) > 0 and len(nums2) > 0:
                        if nums1[0] <= nums2[0]:
                            nums1.pop(0)
                            poped_item_counter += 1
                        else:
                            nums2.pop(0)
                            poped_item_counter += 1
                    elif len(nums1) == 0 and len(nums2) > 0:
                        return float(nums2[median_nr-poped_item_counter-1])
                    elif len(nums2) == 0 and len(nums1) > 0:
                        return float(nums1[median_nr - poped_item_counter - 1])
                if len(nums1) == 0:
                    return float(nums2[0])
                elif len(nums2) == 0:
                    return float(nums1[0])
                return float(nums1[0]) if nums1[0] <= nums2[0] else float(nums2[0])
        else:
            median_nr1 = int(n/2)
            median_nr2 = int(n/2) + 1
            if len(nums1) == 0:
                return 0.5 * (nums2[median_nr1 - 1] + nums2[median_nr2 - 1])
            elif len(nums2) == 0:
                return 0.5 * (nums1[median_nr1 - 1] + nums1[median_nr2 - 1])
            else:
                while poped_item_counter < median_nr1 - 1:
                    if len(nums1) > 0 and len(nums2) > 0:
                        if nums1[0] <= nums2[0]:
                            nums1.pop(0)
                            poped_item_counter += 1
                        else:
                            nums2.pop(0)
                            poped_item_counter += 1
                    elif len(nums1) == 0 and len(nums2) > 0:
                        return 0.5* (nums2[median_nr1-poped_item_counter-1] + nums2[median_nr1-poped_item_counter])
                    elif len(nums2) == 0 and len(nums1) > 0:
                        return 0.5* (nums1[median_nr1-poped_item_counter-1] + nums1[median_nr1-poped_item_counter])
                if len(nums1) == 0:
                    return 0.5*(nums2[0]+nums2[1])
                elif len(nums2) == 0:
                    return 0.5*(nums1[0]+nums1[1])
                else:
                    if nums1[0] <= nums2[0]:
                        l1 = nums1[0]
                        nums1.pop(0)
                        if len(nums1) == 0:
                            l2 = nums2[0]
                            return 0.5 * (l1 + l2)
                        else:
                            return 0.5 * (l1 + nums1[0]) if nums1[0] <= nums2[0] else 0.5 * (l1 + nums2[0])
                    else:
                        l1 = nums2[0]
                        nums2.pop(0)
                        if len(nums2) == 0:
                            l2 = nums1[0]
                            return 0.5 * (l1 + l2)
                        else:
                            return 0.5 * (l1 + nums2[0]) if nums2[0] <= nums1[0] else 0.5 * (l1 + nums1[0])



s = Solution()
# print(s.findMedianSortedArrays([1, 3],[2,4]))
# print(s.findMedianSortedArrays([1, 3],[2]))
# print(s.findMedianSortedArrays([1, 3,5,7],[]))
# print(s.findMedianSortedArrays([],[1,3,5,7]))
print(s.findMedianSortedArrays([1,1,3,4,5,6,7,8,9,10],[2,3]))
print(s.findMedianSortedArrays([1,1,3,4,5,6,7,8,9,10,11,12],[2,3]))

print(s.findMedianSortedArrays([1,1,3,4,5,6,7,8,9],[2,3]))
print(s.findMedianSortedArrays([1,1,3,4,5,6,7,8,9,10,11],[2,3]))
