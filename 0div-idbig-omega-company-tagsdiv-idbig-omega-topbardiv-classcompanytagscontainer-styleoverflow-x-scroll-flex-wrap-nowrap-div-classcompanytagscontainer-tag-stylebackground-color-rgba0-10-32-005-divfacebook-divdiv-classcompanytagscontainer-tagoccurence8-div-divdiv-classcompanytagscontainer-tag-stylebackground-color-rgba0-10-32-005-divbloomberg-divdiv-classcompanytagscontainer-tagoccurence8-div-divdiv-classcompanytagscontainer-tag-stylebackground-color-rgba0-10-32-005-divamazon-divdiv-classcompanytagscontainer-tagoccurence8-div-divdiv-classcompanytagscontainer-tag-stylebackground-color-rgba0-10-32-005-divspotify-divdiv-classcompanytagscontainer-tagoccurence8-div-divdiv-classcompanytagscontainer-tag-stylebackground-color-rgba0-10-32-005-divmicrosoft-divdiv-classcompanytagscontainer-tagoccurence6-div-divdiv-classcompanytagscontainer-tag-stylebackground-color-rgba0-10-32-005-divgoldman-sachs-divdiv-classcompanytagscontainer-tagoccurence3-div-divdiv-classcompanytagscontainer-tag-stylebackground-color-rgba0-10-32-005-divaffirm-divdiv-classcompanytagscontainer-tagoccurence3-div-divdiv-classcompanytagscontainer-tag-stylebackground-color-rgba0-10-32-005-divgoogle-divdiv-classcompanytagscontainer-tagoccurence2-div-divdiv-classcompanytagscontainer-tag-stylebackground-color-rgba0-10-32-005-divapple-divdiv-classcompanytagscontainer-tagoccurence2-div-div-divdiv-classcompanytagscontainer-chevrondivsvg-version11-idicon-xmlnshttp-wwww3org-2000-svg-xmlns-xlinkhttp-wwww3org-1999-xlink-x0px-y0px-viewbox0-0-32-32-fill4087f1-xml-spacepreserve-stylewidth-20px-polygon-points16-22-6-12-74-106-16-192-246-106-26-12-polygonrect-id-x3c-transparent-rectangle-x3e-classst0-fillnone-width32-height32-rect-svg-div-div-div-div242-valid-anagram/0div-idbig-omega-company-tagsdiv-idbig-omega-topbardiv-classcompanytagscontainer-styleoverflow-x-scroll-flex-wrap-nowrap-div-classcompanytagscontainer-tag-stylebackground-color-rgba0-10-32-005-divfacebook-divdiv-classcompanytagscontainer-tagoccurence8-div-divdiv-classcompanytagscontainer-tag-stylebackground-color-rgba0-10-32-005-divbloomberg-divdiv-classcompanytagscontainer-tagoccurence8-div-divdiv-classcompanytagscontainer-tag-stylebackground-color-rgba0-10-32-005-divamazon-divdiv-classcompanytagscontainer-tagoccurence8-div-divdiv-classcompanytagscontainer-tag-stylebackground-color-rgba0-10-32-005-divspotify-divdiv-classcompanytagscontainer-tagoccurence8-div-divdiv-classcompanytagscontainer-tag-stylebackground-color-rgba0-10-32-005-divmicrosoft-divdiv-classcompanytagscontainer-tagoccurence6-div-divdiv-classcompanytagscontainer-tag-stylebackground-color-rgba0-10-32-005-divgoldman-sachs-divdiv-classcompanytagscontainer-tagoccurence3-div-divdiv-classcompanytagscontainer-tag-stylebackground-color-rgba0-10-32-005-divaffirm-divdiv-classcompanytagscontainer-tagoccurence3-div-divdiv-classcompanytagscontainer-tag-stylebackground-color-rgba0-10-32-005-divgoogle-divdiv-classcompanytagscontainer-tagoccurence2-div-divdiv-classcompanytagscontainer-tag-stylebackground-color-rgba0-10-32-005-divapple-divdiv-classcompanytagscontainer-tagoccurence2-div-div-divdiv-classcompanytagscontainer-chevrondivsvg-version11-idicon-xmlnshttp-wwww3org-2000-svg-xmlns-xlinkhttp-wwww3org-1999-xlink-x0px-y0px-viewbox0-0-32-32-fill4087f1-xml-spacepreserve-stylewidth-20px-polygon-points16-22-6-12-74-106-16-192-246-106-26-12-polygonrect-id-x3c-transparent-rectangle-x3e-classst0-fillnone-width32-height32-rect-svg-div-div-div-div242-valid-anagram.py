class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}
        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for j in t:
            if j in s_dic:
                s_dic[j] -= 1
            else:
                return False

        print(s_dic)
        count_zeros = 0
        for i in s_dic.keys():
            if s_dic[i]==0:
                count_zeros+=1

        if count_zeros==len(s_dic):
            return True
        return False