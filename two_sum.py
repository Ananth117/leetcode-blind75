class Solution:
    def twoSum(self, nums, target):
        c={}
        for i,num in enumerate(nums):
            comp = target-num
            if comp in c:
                return [c[comp], i]
            c[num] = i