#https://leetcode.com/problems/convert-the-temperature/description/
class Solution:
        #defineerisin funktsiooni, mis teisendab Celsiuse väärtuse Kelviniks ning Fahrenheitiks
        def convertTemperature(self, Celsius):
            Kelvin = Celsius + 273.15
            Fahrenheit = Celsius * 1.80 + 32.00
            #Lõin tühja listi
            convertTemperature = []
            #Tühja listi lisan Fahrenheiti ning Kelvini väärtused
            convertTemperature = [Kelvin, Fahrenheit]
            #Tagastan teisendatud väärtused
            return convertTemperature
#prindin välja väärtused, mil Celsius on 36.50
print(Solution().convertTemperature(36.50))
