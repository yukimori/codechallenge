x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = [0, 0, 0, 0]
if x2 <= x1:
    if (y2 - y1) > 0:
        x3 = x2 - (x1 - x2)
        y3 = y1
        x4 = x2
        y4 = y1 - (y2 - y1)
    else:
        x3 = x2 + (y1 - y2)
        y3 = y2
        x4 = x1 + (y1 - y2)
        y4 = y1
elif y1 == y2:
    if (x2 - x1) > 0:
        x3 = x2
        y3 = y2 + (x2 - x1)
        x4 = x1
        y4 = y1 + (x2 - x1)
    else:
        x3 = x2
        y3 = y2 - (x1 - x2)
        x4 = x1
        y4 = y1 - (x1 - x2)
print("{} {} {} {}".format(x3, y3, x4, y4))