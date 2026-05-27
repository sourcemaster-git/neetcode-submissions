class Solution:
    def trap(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2

        lmax, rmax = arr[left - 1], arr[right + 1]
        res = 0
        while left <= right:
            if rmax <= lmax:
                res += max(0, rmax - arr[right])

                rmax = max(arr[right], rmax)
                right -= 1

            else:
                res += max(0, lmax - arr[left])
                lmax = max(arr[left], lmax)
                left += 1
        return res