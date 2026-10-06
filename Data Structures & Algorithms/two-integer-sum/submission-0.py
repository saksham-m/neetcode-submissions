class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in hmap:
                return [hmap[num2],i]
            
            hmap[num1] = i

