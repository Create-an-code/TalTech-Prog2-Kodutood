#https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        pikkus = 0
# Programm hakkab lause lõppust ettepoole lugema
        i = len(s)-1
# 2 Kriteeriumi, et lugemisega pole liiga kaugele läinud ja et lõppus poleks tühikuid. Kui on siis loeb niikaua kuniks jõuab esimese täheni
        while i>=0 and s[i] == " ":
            i -= 1
# Kui on jõudnud täheni, siis paneb sõna pikkusele +1 juurde ja liigub niikaua kuniks on sõna lõppu jõudnud ja siis lõpetab programm töö ja annab sõna pikkuse
        while i>=0 and s[i] != " ":
            pikkus +=1
            i -= 1
        return pikkus
