class Solution:
    def singleNumber(self, nums):
        se = set()
        for element in nums:
            if element not in se:
                se.add(element)
            else:
                se.remove(element)
        return (list(se)[0])
a = Solution().singleNumber([2,2,1])
print(a)
