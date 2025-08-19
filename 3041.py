# 20250819
# 3041 N-퍼즐
# 구현

board = [['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','.']]

a = []
for _ in range(4):
    a.append(input().strip())

count = 0
for i in range(4):
    for j in range(4):
        target = board[i][j]
        if target == '.':
            continue
        if a[i][j] == target:
            continue

        found = False
        for k in range(4):
            for l in range(4):
                if a[k][l] == target:
                    count += abs(k - i) + abs(l - j)
                    found = True
                    break
            if found:
                break

print(count)
