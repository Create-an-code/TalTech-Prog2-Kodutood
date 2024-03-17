#https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, numbrid):
        n = len(numbrid)
        loend = {}

        for numbrid in numbrid:
            loend[numbrid] = loend.get(numbrid, 0) + 1
            if loend[numbrid] > n / 2:
                return numbrid