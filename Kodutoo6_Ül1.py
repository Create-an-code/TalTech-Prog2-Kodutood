# https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # muutuja count väärtuseks panen 0
        count = 0
        # listis nums, vaatab iga i väärtuse läbi
        for i in range(len(nums)):
            # listis nums käib igaj väärtuse läbi
            # vaadates, et i < j
            for j in range(i+1,len(nums)):
                # kui i väärtus on sama mis j väärtus, siis
                # leidis indetsed paarid
                if nums[i] == nums[j]:
                    # muutuja count võtab identsete paaride arvu
                    count += 1
        # muutuja count tagastab identsete paaride arvu
        return count