class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        
        prefix_sum = [0] * (len(gain) + 1)
        for i in range(1, len(gain) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + gain[i - 1]
        
        for altitude in prefix_sum:
            max_altitude = max(max_altitude, altitude)
        
        return max_altitude
