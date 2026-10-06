class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = dict()

        for n in nums:
            hmap[n] = 1 + hmap.get(n,0)
        
        arr = []

        for num,cnt in hmap.items():
            arr.append([cnt,num])
        
        arr.sort()
        
        res = []

        while len(res)<k:
            res.append(arr.pop()[1])
        return res