class Solution:
    # Isn't this just a conversion?
    def angleClock(self, hour: int, minutes: int) -> float:
        min_degFrom12 = minutes / 60 * 360
        hour_degFrom12 = hour / 12 * 360 + min_degFrom12/12
        diff_direct = abs(hour_degFrom12 - min_degFrom12)
        diff_around = 360 - max(hour_degFrom12, min_degFrom12) + min(hour_degFrom12, min_degFrom12)
        return min(diff_direct, diff_around)