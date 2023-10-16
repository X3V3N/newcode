class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds={}
        for i in s:
            if i in ds:
                ds[i]+=1
            else:
                ds[i]=1
        for i in t:
            if i not in ds:
                return False
            else:
                ds[i]-=1
        for i in ds:
            if ds[i]!=0:
                return False
        return True
