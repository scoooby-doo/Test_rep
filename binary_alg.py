user_num: int = int(input())

def binary_search(user_num):
    low_num = 0
    max_num = 100
    bot_num = -1
    num_try = 1
    while user_num != bot_num:
        bot_num = (low_num + max_num) // 2
        print(f"Try#{num_try} -- {bot_num}")
        num_try += 1
        if bot_num > user_num:
            max_num = bot_num
        elif bot_num < user_num:
            low_num = bot_num
        else:
            print("YOU LOOSE!!!")

binary_search(user_num)
