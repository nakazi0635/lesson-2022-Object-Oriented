#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def lecture02_01_printHeroStatus() -> None:
    hero_header = []
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(",")
            else :
                data = line.rstrip().split(",")
                hero_data.append(data)
    for i in  range(len(hero_data)):
        print(f'{hero_data[i][1]}のステータスは', end = '')
        for j in range(len(hero_data[i]))[2:6]:
            print(f'{hero_header[j]}:{hero_data[i][j]}', end = ' ')
            print(hero_data)
        print()
    print()


def lecture02_01_printWeaponStatus() -> None:
    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        for line in f:
            if len(weapon_header) == 0:
                weapon_header = line.rstrip().split(",")
            else :
                data = line.rstrip().split(",")
                weapon_data.append(data)
    for i in range(len(weapon_data)):
        print(f'{weapon_data[i][1]}のステータスは', end = '')
        for j in range(len(weapon_data[i]))[2:]:
            print(f'{weapon_header[j]}:{weapon_data[i][j]}', end = ' ')
        print()
    print()


def lecture02_01_printHeroStatusWithWeapon() -> None:
    hero_header = []
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        for line in f:
            hero_data = list(map(str, line.rstrip().split(",")))
            if hero_data[0] == '1':
                hero_name = hero_data[1]
                hero_hp = int(hero_data[2])
                hero_mp = int(hero_data[3])
                hero_atk = int(hero_data[4])
                hero_def = int(hero_data[5])
                hero_age = int(hero_data[6])
                hero_weapon = int(hero_data[7])

    with open('lecture02_Weapon.csv') as f:
        weapon_header = []
        weapon_data = []
        for line in f:
            if len(weapon_header) == 0:
                weapon_header = line.rstrip().split(",")
            else:
                data = line.rstrip().split(",")
                weapon_data.append(data)
    for data in weapon_data:
        if hero_weapon == int(data[0]):
            weapon_name = data[1]
            weapon_hp = int(data[2])
            weapon_mp = int(data[3])
            weapon_atk = int(data[4])
            weapon_def = int(data[5])
            weapon_age = int(data[6])
            break
    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")


if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()