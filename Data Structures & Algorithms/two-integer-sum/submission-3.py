class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = dict()

        for i in range(len(nums)):

            n = nums[i]
            remainder = target - n

            if remainder in h:
                return [h.get(remainder),i]

            h[n] = i