class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for i, num in enumerate(nums):
            # Remove element that's outside the window
            if i > k:
                window.remove(nums[i - k - 1])
            
            # Check if current element already exists in window
            if num in window:
                return True
            
            # Add current element to window
            window.add(num)
        
        return False