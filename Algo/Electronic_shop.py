import sys

def getMoneySpent(keyboards, drives, s):
    res=-1
    for i in keyboards:
        for j in drives:
            if i+j <=s:
                res = max(res,i+j);
    return res
            

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)