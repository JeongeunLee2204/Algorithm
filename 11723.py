#20250719
#11723 집합
#구현
from operator import truediv

n=int(input())
a=[]
def check(a,n):
    if n in a:
        return True
    else:
        return False

def add(a,n):
    if check(a,n):
        return
    else:
        a.append(n)

def remove(a,n):
    if check(a,n):
        a.remove(n)
    else:
        return

def toggle(a,n):
    if check(a,n):
        remove(a,n)
    else:
        add(a,n)


for _ in range(n):
    command = input().split()
    operation = command[0]
    #operation, operand=input().split()
    #실수: operand가 없는 명령도 고려해야함
    if operation == 'add':
        add(a, int(command[1]))
    elif operation == 'remove':
        remove(a, int(command[1]))
    elif operation == 'check':
        print(1 if check(a, int(command[1])) else 0)
    elif operation == 'toggle':
        toggle(a, int(command[1]))
    elif operation == 'all':
        a = [i for i in range(1, 21)]
    elif operation == 'empty':
        a = []
