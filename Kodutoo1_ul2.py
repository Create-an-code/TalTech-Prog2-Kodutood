class Solution:
        def convertTemperature(self, Celsius):
            Kelvin = Celsius + 273.15
            Fahrenheit = Celsius * 1.80 + 32.00
            convertTemperature = []
            convertTemperature = [Kelvin, Fahrenheit]
            return convertTemperature
print(Solution().convertTemperature(36.50))