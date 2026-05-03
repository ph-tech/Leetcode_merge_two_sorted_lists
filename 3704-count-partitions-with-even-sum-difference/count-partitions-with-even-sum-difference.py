class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sums = sum(nums)
        if total_sums % 2 != 0:
            return 0
        
        # Otherwise all partitions are valid
        return len(nums) - 1
        