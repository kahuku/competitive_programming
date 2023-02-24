class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def solve(index, target, dp):
            if index == 0:
                if target % coins[index] == 0:
                    return 1
                return 0
            
            if (index, target) in dp:
                return dp[(index, target)]

            not_take_ways = solve(index - 1, target, dp)

            take_ways = 0
            if coins[index] <= target:
                take_ways = solve(index, target - coins[index], dp)

            dp[(index, target)] = not_take_ways + take_ways
            return not_take_ways + take_ways

        return solve(len(coins) - 1, amount, {})