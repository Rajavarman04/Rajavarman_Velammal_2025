"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

"logic 1:"

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


solution = Solution()
print(solution.climbStairs(2))  
print(solution.climbStairs(3)) 

"logic 2:"

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first, second = 1, 2
        
        
        for i in range(3, n + 1):
            current = first + second
            first, second = second, current
        
        return second


solution = Solution()
print(solution.climbStairs(2))  
print(solution.climbStairs(3))  


        
