class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:

            count = [0]*26

            for cha in s:
                i = ord(cha) - ord('a')
                count[i] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())