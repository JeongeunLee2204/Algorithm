#20250824
#11727 2xn타일링 2
#dp

import sys
input=sys.stdin.readline

tile=[0]*1001
tile[1]=1
tile[2]=3
for i in range(3,1001):
    tile[i]=tile[i-1]+2*tile[i-2]
#print(tile)
n=int(input())
print(tile[n]%10007)
