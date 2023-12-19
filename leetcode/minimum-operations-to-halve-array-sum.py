import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        starting_sum = sum(nums)
        heap = [-num for num in nums]
        heapq.heapify(heap)
        curr_sum = starting_sum
        c = 0
        while curr_sum > starting_sum / 2:
            num = -heappop(heap)
            curr_sum -= num
            heappush(heap, -num / 2)
            curr_sum += num / 2
            c += 1
        return c