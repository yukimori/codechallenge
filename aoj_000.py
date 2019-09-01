for i in range(10):
    for j in range(10):
        if i == 0 or j == 0:
            continue
        ans = i * j
        print("{}x{}={}".format(i, j, ans))