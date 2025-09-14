#20250914
#15829 Hashing
#해시함수

def atoi(s):
    a=[]
    for i in range(len(s)):
        a.append(ord(s[i])-96)
    return a

def hash(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]*pow(31,i)
    return sum%1234567891

n=int(input())
s=input()
print(hash(atoi(s)))