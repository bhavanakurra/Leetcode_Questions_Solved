class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        cnt = 0
        while True:
            if (i==len(s)) or (j==len(t)):
                break
            if s[i]==t[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        if cnt==len(s):
            return True
        return False
                    
        