class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)

        prefix_sum[0] = 1
        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num

            complement = current_sum - k

            if complement in prefix_sum:
                ans += prefix_sum[complement]
            prefix_sum[current_sum] += 1

        return ans