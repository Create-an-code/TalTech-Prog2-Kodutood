#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    #defineerin funktsiooni, mis leiab ülesse numbrid mis on puudu ning asendab üleliigsed
    def findDissappearedNumbers(self, nums: List[int]) -> List[int]:
        #teen numbrite jada hulgaks
        nums_set = set(nums)
        #loon tulemuse jaoks tühja listi
        tulemus = []
        
        #defineerin tingimuse, mis loendab numbrid 1 sammuga 1st alates
        for i in range(1, len(nums)+1):
            #kui numbrit ei olegi seal, siis lisab selle tühja listi
            if i not in nums_set:
                tulemus.append(i)
            #kui number on seal juba olemas, siis jätkab tegevust ning liigub edasi
            else:
                continue
        #tagastab mitte enam tühja listi, vaid arvudega mis olid puudu
        return tulemus
        