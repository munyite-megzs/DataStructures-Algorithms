import bisect
#this module helps to do the binary search automatically
def maximumPosNeg(nums):
        first_non_negative = bisect.bisect_left(nums, 0)
        first_positive = bisect.bisect_right(nums, 0)
        neg = first_non_negative
        pos = len(nums) - first_positive
        return max(pos,neg)

nums = [-3, -2, -1, 0, 0, 1, 2, 3]
nums1 = [-2, -1,0 ,0 , 1 , 2 , 3 ,4]
print(maximumPosNeg(nums))
print(maximumPosNeg(nums1))