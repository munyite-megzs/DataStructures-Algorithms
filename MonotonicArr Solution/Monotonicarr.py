class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc=dec=True
        for i in range(1,len(nums)):
            #check if monotonically decreasing
            if nums[i] > nums[i-1]:
                dec=False
          #check if monotonically increasing
            if nums[i] < nums[i-1]:
                inc=False
        return inc or dec
