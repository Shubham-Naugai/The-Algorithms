# class Solution:
#     def func(self,t,s,i,ans):
#         if(i >= len(t)):
#             print(ans)
#             if(ans == s):
#                 return True
#             return False
#         ans = ans + t[i]
#         v1 = self.func(t,s,i+1,ans)
#         ans = ans[:-1]
#         v2 = self.func(t,s,i+1,ans)
#         if(v1 or v2):
#             return True
#         else:
#             return False
#     def isSubsequence(self, s: str, t: str) -> bool:
#         return self.func(t,s,0,"")
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = ""
        j = 0
        if(len(s) == 0):
            return True
        for i in range(len(t)):
            if(s[j] == t[i]):
                j = j+1
            if(j == len(s)): 
                return True
        return False