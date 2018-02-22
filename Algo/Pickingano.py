import sys

def pickingNumbers(a):
    chk=0
    res=[]
    for i in range(1,len(a)):
        if abs((a[chk]-a[i]))<=0:
            res.append(a[i])
            #res.append(a[chk])
            #print res.append(chk)
    print res
    return len(res)
            
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = pickingNumbers(a)
    print result
