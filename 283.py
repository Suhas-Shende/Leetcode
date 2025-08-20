# Move zeroes at end of list while maintaining the order
# https://leetcode.com/problems/move-zeroes/
# Easy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        for i in range(n):
           if nums[i]!=0:
              temp.append(nums[i])
        
        if temp:
            for i in range(len(temp)):
                nums[i]=temp[i]
            for i in range(len(temp),n):
                nums[i]=0


                
                
          


        
            