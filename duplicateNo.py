#25-06-2020
#Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no = len(nums)
        
        for i in range(no):
            if nums[abs(nums[i])] >= 0: 
                nums[abs(nums[i])] = -nums[abs(nums[i])] 
            else: 
                return abs(nums[i])