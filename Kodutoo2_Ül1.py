#https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution:
    #defineerisin funktsiooni defangIPaddr
    def defangIPaddr(self, address):
        #asendab aadressis punktid [.] tähistusega ning tagastab aadressi sellisel kujul
        return address.replace(".", "[.]") 
