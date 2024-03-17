class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        kokku = 0
        for i in set(nums):
            if nums.count(i) == 1:
                kokku += i
        return kokku
