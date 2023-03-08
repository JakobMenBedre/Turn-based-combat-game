
import random
import sys
import os


classp1 =0
classp2=0
classes = ['1','2','3','4']
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class knight:
    hp =110
    damage = 10
    block = 1
    shield =0.1
    chance = 0
    luck = [19,20]
    sp1dmg = 15
    sp2dmg = 20
    special1cd = 0
    special2cd = 0
    sp1cd=2
    sp2cd=3



class thief:
    hp =80
    damage = 10
    block = 1
    shield =0.3
    chance = 0
    luck = [17,18,19,20]
    sp1dmg = 15
    sp2dmg = 15
    special1cd = 0
    special2cd = 0
    sp1cd=2
    sp2cd=2


class mage:
    hp =90
    damage = 12
    block = 1
    shield =0.2
    chance = 0
    luck = [20]
    sp1dmg = 15
    sp2dmg = 18
    special1cd = 0
    special2cd = 0
    sp1cd=2
    sp2cd=3

class tank:
    hp =150
    damage = 6
    block = 1
    shield =0
    chance = 0
    luck = [20]
    sp1dmg = 10
    sp2dmg = 14
    special1cd = 0
    special2cd = 0
    sp1cd=2
    sp2cd=3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class p1:
    hp =0
    damage = 0
    block = 1
    shield =0
    chance = 0
    luck = [0]
    sp1dmg = 0
    sp2dmg = 0
    special1cd = 0
    special2cd = 0
    sp1cd=0
    sp2cd=0

class p2:
    hp = 0
    damage = 0
    block = 1
    shield = 0
    chance = 0
    luck = [0]
    sp1dmg =0
    sp2dmg=0
    special1cd = 0
    special2cd = 0
    sp1cd=0
    sp2cd=0



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

while classp1 !=classes:

    print("select a class [PLAYER 1]")
    print("insert 1 for knight      - 110hp - 10 damage - 90% block - 10% luck - 15 sp1 damage  (2cd) - 20 sp2 damage (3cd)")
    print("insert 2 for thief      - 80hp - 10 damage - 70% block - 20% luck - 15 sp1 damage  (2cd) - 15 sp2 damage (2cd)")
    print("insert 3 for mage      - 90hp - 12 damage - 80% block - 5% luck - 15 sp1 damage  (2cd) - 18 sp2 damage (2cd)")
    classp1=input("insert 4 for tank      - 150hp - 6 damage - 100% block - 5% luck - 10 sp1 damage  (2cd) - 14 sp2 damage (3cd)")
    if classp1 == '1':
        p1 = knight
        os.system('cls')
        break


    elif classp1 == '2':
        p1=thief
        os.system('cls')
        break

    elif classp1 =='3':
        p1=mage
        os.system('cls')
        break


    elif classp1 =='4':
        p1=tank
        os.system('cls')
        break

    else:
        print("insugnificant input")
        os.system('cls')
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

while classp2 !=['1','2','3','4']:

    print("select a class [PLAYER 2]")
    print("insert 1 for knight      - 110hp - 10 damage - 90% block - 10% luck - 15 sp1 damage  (2cd) - 20 sp2 damage (3cd)")
    print("insert 2 for thief      - 80hp - 10 damage - 70% block - 20% luck - 15 sp1 damage  (2cd) - 15 sp2 damage (2cd)")
    print("insert 3 for mage      - 90hp - 12 damage - 80% block - 5% luck - 15 sp1 damage  (2cd) - 18 sp2 damage (2cd)")
    classp1=input("insert 4 for tank      - 150hp - 6 damage - 100% block - 5% luck - 10 sp1 damage  (2cd) - 14 sp2 damage (3cd)")
    if classp2 == '1':
        p2=knight
        os.system('cls')
        break

    elif classp2 == '2':
        p2=thief
        os.system('cls')
        break


    elif classp1 =='3':
        p2=mage
        os.system('cls')
        break


    elif classp1 =='4':
        p2=tank
        os.system('cls')
        break

    elif classp2 != [classes]:
        print("insugnificant input")
        os.system('cls')
    


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

turn = 1
while p1.hp and p2.hp != 0:
    while turn == 1:
            print("what will you do? {p1}")
            print("special 1 is at", p1.special1cd, "cooldown")
            print("special 2 is at", p1.special2cd, "cooldown")
            action=input("||| attack: e | special 1: d | special 2: f | block: r |||")
            

            if action=="e":
                p1.damage = 10
            elif action=="d":
                if p1.special1cd >0:
                    p1.damage = 10
                else:
                    p1.damage = 20
                    p1.special1cd = p1.sp1cd
            elif action == "f":
                if p1.special2cd >0:
                    p1.damage = 10
                else:
                    p1.damage = 15
                    p1.special2cd = p1.sp2cd
            elif action == "r":
                p1.block = p1.shield
            os.system('cls')
            turn = 2

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    while turn ==2:
            print("what will you do? {p2}")
            print("special 1 is at", p2.special1cd, "cooldown")
            print("special 2 is at", p2.special2cd, "cooldown")
            action=input("||| attack: e | special 1: d | special 2: f | block: r |||")
            if action=="e":
                p2.damage = 10
            elif action=="d":
                if p2.special1cd >0:
                    p2.damage = 10
                else:
                    p2.damage = 20
                    p2.special1cd = p2.sp1cd
            elif action == "f":
                if p2.special1cd >0:
                    p2.damage = 10
                else:
                    p2.damage = 15
                    p2.special2cd = p2.sp2cd
            elif action == "r":
                p2.block = p2.shield
            os.system('cls')
            turn = 3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    while turn==3:
        p1.chance=random.randint(1, 20)
        if p1.chance == 1:
            p1.damage = p1.damage * 0.5
        elif p1.chance == str(p1.luck):
            p1.damage = p1.damage * 1.5
        
        p2.chance=random.randint(1, 20)
        if p2.chance == 1:
            p2.damage = p2.damage * 0.5
        elif p2.chance == 20:
            p2.damage = p1.damage * 1.5

        p2.hp=p2.hp-p1.damage*p2.block
        print(p1.hp, "hp left for player 2")
        if p2.hp <= 0:
            print("Player 1 has emerged victorious!")
            sys.exit()
        else:
            p1.hp=p1.hp-p2.damage*p1.block
            print(p2.hp, "hp left for player 1")
        if p1.hp <= 0:
            print("Player 2 has emerged victorious!")
            sys.exit()
        p1.damage = 0
        p2.damage = 0
        p1.block = 1
        p2.block = 1
        p1.special1cd = p1.special1cd - 1
        p1.special2cd = p1.special2cd - 1
        p2.special1cd = p2.special1cd - 1
        p2.special2cd = p2.special2cd - 1
        if p1.special1cd <=0:
            p1.special1cd = 0
        if p1.special2cd <=0:
            p1.special2cd = 0
        if p2.special1cd <=0:
            p2.special1cd = 0
        if p2.special2cd <=0:
            p2.special2cd = 0
        turn=1
sys.exit()