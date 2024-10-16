class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Elizabeth
        Truphena
        Risper
        """
         #initialize the variables to an empty list
        single_digit_nums=[]
        double_digit_nums=[]
       #condition to add the single digits and double digits to their respective lists
        for i in nums:
            if 0<=i<=9:
                single_digit_nums.append(i)#adds each element between 0 and 9

        for i in nums:
            if 10<=i<=99:
                double_digit_nums.append(i)#adds each element between 10 and 99
        #sum of the single and double digits
        sum_single_digits=sum(single_digit_nums)
        sum_double_digits=sum(double_digit_nums)
        #scenario 1 if Alice receives sum of single digits
        Alice_single=sum_single_digits
        Bob_double=sum_double_digits
        #scenario 2 if Alice receives sum of double digits
        Alice_double=sum_double_digits
        Bob_single=sum_single_digits
        #condition if Alice receives more than Bob
        if(Alice_single>Bob_double) or (Alice_double>Bob_single):
            return True
        else:
            return False
        
    print(canAliceWin.__doc__)

solution=Solution()
#nums = [1,2,3,4,10]
#nums = [1,2,3,4,5,14]
nums = [5,5,5,25]
print(solution.canAliceWin(nums))


