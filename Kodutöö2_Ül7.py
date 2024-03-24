class Solution:
    def containsDuplicate(self, numbrid):
        #Sorteerib
        numbrid.sort()
        for i in range(len(numbrid)-1):
            #Kui number kattub siis vastus on true
            if numbrid[i] == numbrid[i+1]:
                return True
        #Kui number ei kattu, siis vastus false
        return False