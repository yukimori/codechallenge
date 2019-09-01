a, b = [int(i) for i in input().split()]
value = a * b
if  value % 2 == 0:
    ans = "Even"
else:
    ans = "Odd"
print("{}".format(ans))
    