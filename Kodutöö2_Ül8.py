class Solution(object):
    def smallerNumbersThanCurrent(self, numbrid):
        alg = sorted(numbrid)
    kaart = {}
    vastus = []
    for i in range(len(alg)):
        if alg[i] not in kaart:
            kaart[alg[i]] = i
    for i in range(len(numbrid)):
        vastus.append(kaart[numbrid[i]])
    return vastus