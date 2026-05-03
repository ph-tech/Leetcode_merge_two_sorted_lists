class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix = [0] * (n + 1)
        prefix[0] = 1
        
        max_d = deque()
        min_d = deque()
        
        j = 0
        
        for i in range(n):
            # Maintain max deque
            while max_d and nums[max_d[-1]] <= nums[i]:
                max_d.pop()
            max_d.append(i)
            
            # Maintain min deque
            while min_d and nums[min_d[-1]] >= nums[i]:
                min_d.pop()
            min_d.append(i)
            
            # Shrink window if invalid
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if max_d[0] == j:
                    max_d.popleft()
                if min_d[0] == j:
                    min_d.popleft()
                j += 1
            
            # Compute dp
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % MOD
            
            # Update prefix
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % MOD
        
        return dp[n]