class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)-1):
            for i2 in range(i+1, len(nums)):
                if nums[i]+ nums[i2] == target:
                    return [i, i2]
        