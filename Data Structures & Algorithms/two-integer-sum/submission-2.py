class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap ={}

        for i,n in enumerate(nums):
            m = target - n
            
            if m in hmap:
                return [hmap[m],i]
            hmap[n] = i
        