class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        vastus = []
        for el in range(1,n+1):
            if el%3==0 and el%5==0:
                vastus.append("FizzBuzz")
            elif el%3==0:
                vastus.append("Fizz")
            elif el%5==0:
                vastus.append("Buzz")
            else:
                vastus.append(str(el))
        return vastus
            
        
