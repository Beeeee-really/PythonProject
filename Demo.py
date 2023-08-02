import random

while True:
    player = input("输入:(1:剪刀 2:石头 3:布)")

    computer = str(random.randint(1, 3))
    computer_ = ""
    if computer == "1":
        computer_ = "剪刀"
    elif computer == "2":
        computer_ = "石头"
    elif computer == "3":
        computer_ = "布"
    else:
        computer_ = "error"
        break
    print("电脑:" + computer_)
    if player == computer:
        print("平局")
    elif player == "1" and computer == "2" or player == "2" and computer == "3" or player == "3" and computer == "1":
        print("输了:(")
    elif player == "1" and computer == "3" or player == "2" and computer == "1" or player == "3" and computer == "2":
        print("赢了:)")
    else:
        print("你在输入什么？？？？？")

    i = 0
    while i < 10000:
        print("-", end="")
        i += 1
    print("")
