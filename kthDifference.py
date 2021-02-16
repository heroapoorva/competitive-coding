class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def bound(i):
            count=0
            l=0
            for r,x in enumerate(nums):
                while x - nums[l] > i:
                    l += 1
                count += r - l
            return count>=k
        
        nums.sort()
        l=0
        r=nums[-1]-nums[0]
        while l<r:
            m= (l+r)//2
            if bound(m):
                r=m
            else:
                l=m+1
        return l
