class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_hand_degrees_per_minute = 1/60 * 360
        hour_hand_degrees_per_minute = 1/12 * 1/60 * 360

        hour_degrees = (60 * hour + minutes) * hour_hand_degrees_per_minute
        hour_degrees += 360
        hour_degrees %= 360

        minute_degrees = (minutes - 60) * minute_hand_degrees_per_minute
        minute_degrees += 360
        minute_degrees %= 360
        
        ans = max(minute_degrees, hour_degrees) - min(minute_degrees, hour_degrees)
        return ans if ans <= 180 else 360 - ans