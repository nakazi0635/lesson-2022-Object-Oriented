#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lecture01_01() -> None:
# 辞書型のオブジェクトhを宣言すること
# hに，キー（“ID”）に自身の学籍番号を代入すること．
# hに，キー（“attributes”）にタプル型で名前と年齢と性別(例：(“名前”，22，”男”))を代入すること．

# hをprint関数で出力せよ．
# hのキー一覧をprint関数で出力せよ．
# hのキーの型をprint関数で出力せよ．
# h[“attributes”]の型をprint関数で出力せよ．
# h[“attributes”]の各要素を１行づつprint関数で出力せよ．(for e in attr:)
# h[“attributes”]の各要素の型を１行づつprint関数で出力せよ．(for e in attr:)
    h={}
    h["ID"] = 'k21085'
    h["attributes"] = ('中嶋優一', 20, '男')

    print(h)
    # print(h.items())
    print(h.keys())
    # print(h.values())
    for x in h.keys():
        print(type(x)) # キー一覧を出力
    print(type(h["attributes"]))
    for k in h["attributes"]:
        print(k)
    for k in h["attributes"]:
        print(type(k))
    

if __name__ == '__main__':
    lecture01_01()