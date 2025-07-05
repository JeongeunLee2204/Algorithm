#20250705
#11050 이항 계수 1
#조합론-이항계수 공식(nCk=n!/k!(n-k)!)

#이항계수 공식이 생각 안나서 검색했다
#실수: Python에서 range 함수는 종료값을 포함하지 않는 특성이 있으므로, 특정 값 n까지 포함하여 반복을 수행하려면 range(n+1)과 같이 종료값에 1을 더해야함
def factorial(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

n,k=map(int,input().split())
print(int((factorial(n)/(factorial(k)*factorial(n-k)))))