import random
class Solution:
    def partition(self, nums:List[int], low: int, high: int) -> int:
        random_p = random.randint(low, high)

        nums[random_p], nums[high] = nums[high], nums[random_p]
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quicksort(self, nums: List[int], low:int, high: int):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quicksort(nums, low, pi - 1)
            self.quicksort(nums, pi + 1, high)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
        