N, M = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(0, N)]

ab.sort()

ans = 0
for a, b in ab:
    if M > b:
        ans += a*b
        M = M - b
    else:
        ans += a*M
        break
print(ans)