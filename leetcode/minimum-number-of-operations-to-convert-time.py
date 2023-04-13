class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h, m = current.split(":")
        h, m = int(h), int(m)
        target_h, target_m = correct.split(":")
        target_h, target_m = int(target_h), int(target_m)
        curr_sum, target_sum = 60 * h + m, 60 * target_h + target_m
        ops = 0
        while target_sum - curr_sum >= 60:
            curr_sum += 60
            ops += 1
        while target_sum - curr_sum >= 15:
            curr_sum += 15
            ops += 1
        while target_sum - curr_sum >= 5:
            curr_sum += 5
            ops += 1
        while target_sum - curr_sum >= 1:
            curr_sum += 1
            ops += 1
        return ops