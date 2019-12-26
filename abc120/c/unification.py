qube = input()

red = qube.count("0")
blue = qube.count("1")

ans = min(red, blue) * 2
print(ans)