class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        # print(l)
        
        res = ""
        for i in range(len(l)-1,-1,-1):
            # print(i,l[i],"res-",res,"-end")
            if l[i]=='':
                continue
            res += l[i].strip()
            if i>0:
                res += " "
                
        if res[-1] == " ":
            res = res[:-1]
            
        # print(res)
        
        return res