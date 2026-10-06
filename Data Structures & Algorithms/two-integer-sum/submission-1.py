class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i,n in enumerate(nums):
            remainder = target - nums[i]

            if remainder in hmap:
                return [hmap[remainder], i]

            hmap[n] = i