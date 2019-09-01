"""
n q
name1 time1
name2 time2
...
nameN timeN

n: プロセス数
q: クオンタム（CPUの最大処理時間）
name: プロセス名
time: 必要な処理時間
"""
def resolve2():
    pass


def resolve1():
    """
    自分で書いたやつ
    listは条件文では要素があるとTrue，空だとFalseを返却する
    """
    complete_process = []
    if process:
        print("process is True")

    elapsed_time = 0
    while process:
        name, time = process.pop(0)
        print("pop:", name, ":", time)
        if time <= p:
            elapsed_time += time
            complete_process.append((name, elapsed_time))
        else:
            process.append((name, (time-p)))
            elapsed_time += p

        print(elapsed_time, ":", process)
    for elem in complete_process:
        print(elem[0], " ", elem[1])
    

if __name__ == "__main__":
    # 入力情報の取得
    n, p = map(int, input().split())
    print(n, p)
    
    process = []
    process_info = {}
    for _ in range(n):
        name, time = input().split()
        process.append((name, int(time)))
        process_info[name] = time

    print(process)
    print(type(process[0][0]), type(process[0][1]))
    resolve1()