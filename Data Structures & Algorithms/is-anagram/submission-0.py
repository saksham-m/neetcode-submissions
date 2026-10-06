class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmapS, hmapT = {}, {}

        n = len(s)
        m = len(t)

        if n != m: 
            return False
        
        for i in range(0,n):
            hmapS[s[i]] = 1+ hmapS.get(s[i],0)

        for i in range(0,n):
            hmapT[t[i]] = 1+ hmapT.get(t[i],0)
        
        return hmapS == hmapT

            