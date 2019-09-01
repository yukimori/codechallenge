s = input()
w = int(input())

i = 0
ans = ""
while i+w < len(s):
    ans = ans + (s[i:i+w])[0]
    i = i + w

ans = ans + (s[i:])[0]
print(ans)
