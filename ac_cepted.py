S = input()

if S.startswith("A") and S[2:-1].count("C") == 1 and S[1].islower() and S[-1].islower():
    deleted_S = S[2:-1].replace("C", "")
    if len(deleted_S) == 0:
        print("AC")
    elif deleted_S.islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")