#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        s = len(nums)
        while i < s:
            if nums[i] == val:
                #kui indeksil i on väärtus sama, mis meie soovitud kustutatav, siis popime selle listist
                nums.pop(i)
                i-=1
                # -i tuleb, sest kui popime listist list[1] väärtuse [0,1,1,2] 1, siis ,muutub list selliseks [0,1,2]  
                # sellel listil on nüüd nihkunud elemendid, ning uuel listil ei kontrolli me list[1] väärtust
                #kuid peame seda tegema, sest pärast popimst liikus sinna uus mittesoovitud väärtus
            i+=1
            s = len(nums)
        return (len(nums))
