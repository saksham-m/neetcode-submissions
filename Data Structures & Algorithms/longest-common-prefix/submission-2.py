class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 300
        ans = ""
        for s in strs:
            min_len = min(min_len,len(s))

        for i in range(min_len):
            cur = strs[0][i]
            for s in strs:
                if s[i] != cur:
                    return ans
            
            ans += cur
        return ans