class Solution:
    def canWinNim(self, n: int) -> bool:
        if not n % 4 == 0:
        #Ülesanne oli lihtsam, kui arvasin. ainuke viis, kuidas võita on alustada kivide arvuga, mis ei jagu neljaga.
            return True
        else:
            return False
