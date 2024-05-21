class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
          #Lihtsalt kontrollime, kas selline substring on s-is sees
            return 0
        elif s.count('A') >= 2:
        #Kasutame counti, sest et siin pole tähtsust, kas nad on järjest või mitte, tahame lihtsalt 'A' esinemise arvu teada saada
            return 0
        #Kui ülemised kaks ei tagasta False'i, siis järelikult peab olema kõik korras, tagastame True
        else:
            return 1

# https://leetcode.com/problems/student-attendance-record-i/
