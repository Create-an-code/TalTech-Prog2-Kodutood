# https://leetcode.com/problems/find-words-containing-character/
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # loon tulemuse jaoks tühja listi
        tulemus_list = []
        # vaatab igat väärtust listist words
        for i in range(len(words)):
            # kui x väärtus ehk tähed on listis words
            if x in words[i]:
                # Siis lisab need tulemus_listi
                tulemus_list.append(i)
        # tagastab tulemus listi
        return tulemus_list