class Solution:
    def merge(self, nums: List[int], left: int, mid: int, right: int):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = nums[left + i]
        for j in range(n2):
            R[j] = nums[mid + 1 + j]
        
        k = left
        i = 0
        j = 0

        while i < n1 and j < n2:
            if L[i]  <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        while i < n1:
            nums[k] = L[i]
            k += 1
            i += 1
        
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1
    
    def mergeSort(self, nums: List[int], left: int, right: int):
        if left < right:
            mid = left + (right - left) // 2

            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums