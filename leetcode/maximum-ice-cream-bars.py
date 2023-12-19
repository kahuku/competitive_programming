class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = 0
        while coins > 0 and n < len(costs):
            if costs[n] <= coins:
                coins -= costs[n]
                n += 1
            else:
                break

        return n