guess=-1
number=7
while guess!=number:
    guess=int(input("输入数字"))
    if guess>number:
        print("猜测的数大了")
    elif guess<number:
        print("猜测的数小了")
    elif guess==number:
        print("恭喜猜对数")
    