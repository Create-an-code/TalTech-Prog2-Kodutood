#https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        #määran loendi väärtuseks 0
        loend = 0
        #loon tingimuse, mil otsib listist iga töötaja tunnid
        for i in hours:
            #loon tingimuse, et kui töötaja tunnid on suuremad
            #kui eesmärk, siis liidab loendile 1 juurde ning tagastab loendi
            if i >= target:
                loend += 1
        #tagastab loendi loendatud arvuga, mitu töötajat oli suurema või võrdse tunniga kui eesmärk
        return loend