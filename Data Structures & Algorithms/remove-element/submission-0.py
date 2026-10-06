class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        k = n

        while i<k:
            print(nums,k)
            if nums[i] == val:
                print(nums[i],nums[k-1])
                nums[i],nums[k-1] = nums[k-1],nums[i]
                k -= 1
            else:
                i+=1
        
                
        return k