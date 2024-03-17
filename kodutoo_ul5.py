class Solution:
    def average(self, salary: List[int]) -> float:
        maksimum = max(salary)
        miinimum = min(salary)
        summa = 0
        mitu = len(salary) - 2
        for el in salary:
            if el == maksimum:
                continue
            elif el == miinimum:
                continue
            else:
                summa += el

        return summa / mitu    
