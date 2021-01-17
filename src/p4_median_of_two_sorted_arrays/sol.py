from typing import List

class Solution:

    def getMedian(self, nums: List[int]) -> float:
        if len(nums) == 0:
            return 0
        if len(nums) % 2 == 0:
            return (nums[int(len(nums)/2)-1] + nums[int(len(nums)/2)])/2
        else:
            return nums[int(len(nums)/2)]

    def maxOf(self, nums1: List[int], nums2: List[int]) -> int:
        result = None
        if len(nums1) > 0:
            result = nums1[-1]
        if len(nums2) > 0 and (result == None or nums2[-1] > result):
            result = nums2[-1]
        return result
    
    def minOf(self, nums1: List[int], nums2: List[int]) -> int:
        result = None
        if len(nums1) > 0:
            result = nums1[0]
        if len(nums2) > 0 and (result == None or nums2[0] < result):
            result = nums2[0]
        return result


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while(True):
            left1 = nums1[0:int(len(nums1)/2)]
            right1 = nums1[int(len(nums1)/2):]
            left2 = nums2[0:int((len(nums2)+1)/2)]
            right2 = nums2[int((len(nums2)+1)/2):]

            l11 = len(left1)
            l21 = len(left2)
            l12 = len(right1)
            l22 = len(right2)

            max_l = self.maxOf(left1, left2)
            min_r = self.minOf(right1, right2)
                
            if max_l == None:
                return self.getMedian(right1)
            if min_r == None:
                return self.getMedian(left2)
            
            if max_l <= min_r:
                if l11 + l21 == l12 + l22:
                    return (max_l + min_r) / 2
                if l11 + l21 > l12 + l22:
                    return max_l
                else:
                    return min_r
            
            if l11 > 0 and l22 > 0 and left1[-1] >= right2[0]:
                new_nums1 = left1
                new_nums2 = right2

                if l21 < l12:
                    new_nums1 = left1[l12 - l21:]
                    if left1[l12-l21-1] > right2[-1]:
                        new_nums2[-1] = left1[l12-l21-1]

                if l21 > l12:
                    new_nums2 = right2[0:l22-l21+l12]
                    if left1[0] > right2[l22-l21+l12]:
                        new_nums1[0] = right2[l22-l21+l12]
                
            elif l21 > 0 and l21 > 0 and left2[-1] >= right1[0]:
                new_nums1 = right1
                new_nums2 = left2

                if l11 < l22:
                    new_nums2 = left2[l22 - l11:]
                    if left2[l22 - l11-1] > right1[-1]:
                        new_nums1[-1] = left2[l22 - l11-1]

                if l11 > l22:
                    new_nums1 = right1[0:l12 - l11 + l22]
                    if left2[0] > right1[l12 - l11 + l22]:
                        new_nums2[0] = right1[l12 - l11 + l22]


            nums1 = new_nums2
            nums2 = new_nums1



solution = Solution()

print(solution.findMedianSortedArrays([3,4,5,6],[1,2]))