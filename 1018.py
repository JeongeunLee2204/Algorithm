#20250708
#1018 체스판 다시 칠하기
#구현

n,m=map(int,input().split())
a=[]
result=[]
b=[]
ex1 = 'WBWBWBWB' #W로 시작하는 경우, B로 시작하는 경우 둘다 처리 위해 패턴 2개 입력
ex2 = 'BWBWBWBW'
def isCheckBoard(board, ex1, ex2): #8회 검사하되 조건문으로 패턴만 변경하기
    count = 0
    for i in range(8):
        pattern = ex1 if i % 2 == 0 else ex2
        for j in range(8):
            if board[i][j] != pattern[j]:
                count += 1
    return count #바꿔야하는 칸수 반환

for i in range(n): #전체 판 입력받기
    line=input()
    a.append(line)
for i in range(n - 7): # 8회/8회 반복하여 체스판 b에 추출
    for j in range(m - 7):
        b = []
        for k in range(8):
            b.append(a[i + k][j:j + 8]) #행은 인덱스로 증가, 열은 slicing으로 8칸 추출
        #print(b)
        result.append(isCheckBoard(b,ex1,ex2))
        result.append(isCheckBoard(b,ex2,ex1))
print(min(result))

#print(a)
