class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
          #assign increasing and decreasing with True
        increasing=True
        decreasing=True
        j=len(nums)#length of the array

        for i in range (0,j-1):#loop through the array
            if nums[i]>nums[i+1]:#checks if the current alue is greater than the next value
                increasing=False#returns false if the array is not increasing
            if nums[i]<nums[i+1]:#checks if the current value is less than the next value
                decreasing=False#returns false  if the array is not decreasing
        return increasing or decreasing
    #print(isMonotonic.__doc__)
solution=Solution()
nums = [1,2,2,3]
print(solution.isMonotonic(nums))
nums=[6,5,4,4]
print(solution.isMonotonic(nums))
nums=[1,3,2]
print(solution.isMonotonic(nums))
    
