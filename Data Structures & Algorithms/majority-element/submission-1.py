class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num != candidate:
                count -= 1
            else:
                count += 1
        n = len(nums)
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > n // 2:
            return candidate
        else:
            return -1