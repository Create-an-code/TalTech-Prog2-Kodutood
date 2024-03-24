class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        pudelite_kogus = 0
        tyhjad_pudelid = 0
        while numBottles > 0:
            pudelite_kogus = pudelite_kogus + numBottles
            tyhjad_pudelid += numBottles
            numBottles = tyhjad_pudelid//numExchange
            tyhjad_pudelid = tyhjad_pudelid%numExchange
        return pudelite_kogus
