class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left, right = 0, len(nums) - 1
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    print(left, right)
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < n and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans