import random

# 隨機生成一個1到100的整數
target_number = random.randint(1, 100)

# 開始猜數字遊戲
while True:
    guess = int(input("猜一個1到100的數字："))
    if guess > target_number:
        print("太大了!")
    elif guess < target_number:
        print("太小了!")
    else:
        print("猜對了!")
        break
