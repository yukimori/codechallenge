"""
https://atcoder.jp/contests/abc123/tasks/abc123_c

6都市 1,2,3,4,5,6
5交通機関
 電車 1->2 1分 A人まで乗れる
 バス 2->3 1分 B人まで乗れる
 タクシー 3->4 1分 C人まで乗れる
 飛行機 4->5 1分 D人まで乗れる
 船 5->6 1分 E人まで乗れる

 それぞれの交通機関は整数時刻に都市から出発
 N人のグループが都市1におり、全員都市6に移動したい
 最短何分かかる？
"""

import math

def my_solve2():
    """
    最短時間はもっとも移動可能人数が少ない区間に依存する
    """
    num = int(input())
    transpotations = []
    for _ in range(5):
        transpotations.append(int(input()))

    # print(transpotations, min(transpotations))
    # 最も移動可能人数が少ない区間の抽出
    bottleneck = min(transpotations)

    # 移動時間．切り上げの必要あり
    time = math.ceil(num / bottleneck)

    time += 4
    return time


def my_solve():
    """
    未完成
    現在の人の分布と1分後の人の分布を分けて考えるために2つの人分布リストが必要
    この方法では制限時間内に計算を終了することができない
    """
    num = int(input())
    # print("num: {}".format(num))
    traffic_a = int(input())
    traffic_b = int(input())
    traffic_c = int(input())
    traffic_d = int(input())
    traffic_e = int(input())

    city_people_num = [num, 0, 0, 0, 0, 0]

    time = 0
    # TODO: 現在の人の分布と1分後の人の分布を分けて考えるために2つのリストが必要
    while city_people_num[5] < num:
        #print(city_people_num)
        # 1->2
        if city_people_num[0] >= traffic_a:
            city_people_num[0] -= traffic_a
            city_people_num[1] += traffic_a
        else:
            city_people_num[1] += city_people_num[0]
            city_people_num[0] = 0
        #print(city_people_num)
        time += 1
        # 2->3
        if city_people_num[1] >= traffic_b:
            city_people_num[1] -= traffic_b
            city_people_num[2] += traffic_b
        else:
            city_people_num[2] += city_people_num[1]
            city_people_num[1] = 0
        #print(city_people_num)
        time += 1
        # 3->4
        if city_people_num[2] >= traffic_c:
            city_people_num[2] -= traffic_c
            city_people_num[3] += traffic_c
        else:
            city_people_num[3] += city_people_num[2]
            city_people_num[2] = 0
        time += 1
        # 4->5
        if city_people_num[3] >= traffic_d:
            city_people_num[3] -= traffic_d
            city_people_num[4] += traffic_d
        else:
            city_people_num[4] += city_people_num[3]
            city_people_num[3] = 0
        time += 1
        # 5->6
        if city_people_num[4] >= traffic_e:
            city_people_num[4] -= traffic_e
            city_people_num[5] += traffic_e
        else:
            city_people_num[5] += city_people_num[4]
            city_people_num[4] = 0
        time += 1
        #print("time {}".format(time))
        #print(city_people_num)

    return time

print(my_solve2())