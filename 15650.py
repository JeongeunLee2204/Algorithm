#20250902
#15650 n과 m(2)
#백트래킹,bfs

n,m=map(int, input().split())
result = []

def dfs(start, depth):
    #print(result)
    if depth==m:
        print(*result)
        return
    for i in range(start, n + 1):
        result.append(i)
        dfs(i + 1, depth + 1)  # 다음 숫자는 i+1부터
        result.pop()

dfs(1, 0)
