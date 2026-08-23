class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        if k > len(nums):
            d  = {}
            for i in range(len(nums)):
                if nums[i] in d:
                    return True
                else:
                    d[nums[i]] = i
            return False
        if len(nums) == 1 and k == 1:
            return False
        d = {}
        for i in range(k + 1):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i

        n = len(nums)
        for i in range(k + 1, n):
            del d[nums[i - k - 1]]
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i
        return False