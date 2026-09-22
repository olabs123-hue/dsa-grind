# ======================================
# LeetCode Problem: convert the temperature
# Language: python3
# Link: https://leetcode.com/problems/convert-the-temperature/
# Synced by: LinkCode
# Date: 9/22/2026, 5:13:45 PM
# ======================================


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15                                
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]