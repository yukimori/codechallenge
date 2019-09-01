a, b, c, d = map(int, input().split())
#print("{} {} {} {}".format(a, b, c, d))

ab = a * b
cd = c * d

if ab > cd:
    ans = ab
elif ab < cd:
    ans = cd
else:
    ans = ab

print("{}".format(ans))