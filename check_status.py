class Solution:
    def check (a,b,flag):
        if (a<0 and b<0) and flag:
            return True
        elif (a < 0 and b >0) or (a > 0 and b <0) and (not flag):
            return True
        else:
            return False
    
sol = Solution

print(sol.check(1,-1,False))
print(sol.check(-1,1,True))