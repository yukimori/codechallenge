import numpy as np
import pandas as pd
import pytest

"""
 pytest -vvv --capture=no analysis.py
 * --capture=no テストをpassしてもprintを表示させる
"""

# test間で共有する
@pytest.fixture(scope="module")
def load_data():
    train = pd.read_csv('./data/titanic/train.csv')
    test = pd.read_csv('./data/titanic/test.csv')

    # 学習データを特徴量と目的変数に分ける
    train_x = train.drop(['Survived'], axis=1)
    train_y = train['Survived']

    # テストデータは特徴量のみなので、そのままでよい
    # コピーはする
    test_x = test.copy()

    print(train_x)
    print(train_y)

    return (train_x, train_y, test_x)



def create_feature(train_x, train_y, test_x):
    from sklearn.preprocessing import LabelEncoder

    # 変数PassengerIdを除外する
    train_x = train_x.drop(['PassengerId'], axis=1)
    test_x = test_x.drop(['PassengerId'], axis=1)

    # 変数Name, Ticket, Cabinを除外する
    train_x = train_x.drop(['Name', 'Ticket', 'Cabin'], axis=1)
    test_x = test_x.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    print("-- before label encoding --")
    print(train_x)

    # それぞれのカテゴリ変数にlabel encodingを適用する
    for c in ['Sex', 'Embarked']:
        # 学習データに基づいてどう変換するかを定める
        le = LabelEncoder()
        le.fit(train_x[c].fillna('NA'))

        # 学習データ、テストデータを変換する
        train_x[c] = le.transform(train_x[c].fillna('NA'))
        test_x[c] = le.transform(test_x[c].fillna('NA'))
        
    print("-- after label encoding --")
    print(train_x)


def test_create_feature(load_data):
    create_feature(load_data[0], load_data[1], load_data[2])


#def test_load_data():
#    load_data()