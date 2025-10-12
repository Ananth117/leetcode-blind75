class Solution:
    def longestConsecutive(self, nums):
        count, current =0, 0
        N = {}
        for n in nums:
            N[n]=1
        for n in N.keys():
            if n-1 in N.keys():
                continue
            current=1
            while n+1 in N.keys():
                n+=1
                current+=1
            count = max(current, count)
        return count