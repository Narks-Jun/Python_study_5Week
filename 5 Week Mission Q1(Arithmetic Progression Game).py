# 1:1 은 2를 선점한 사람이 이후 4개 숫자만 채우면 필승이다

def user_input(x) :
    while True :
        x_input = input("User turn-Plase enter number:").split()
        try :
            if int(x_input[0]) <= 0:
                print("Please enter a number greater than 0.")
                continue
            if len(x_input) > 3:
                print("You can only enter up to 3 numbers.")
                continue
            t = "None"
            if int(x_input[0]) - 1 != int(x[-1]) :
                print("Please enter consecutive numbers")
                continue
            for i in range(1,len(x_input)) :
                if int(x_input[i])-1 != int(x_input[i-1]) :
                    print("Please enter consecutive numbers2.")
                    t = False
                    break
            if t is False :
                continue
        except :
            print("Please enter numeric input.")
            continue
        print("현재 숫자:",x_input[-1])
        return x_input

def computer_input(y) :
    import random
    computer_turn_num = random.randint(1, 3)
    list_com = [i for i in range(1, computer_turn_num+1)]
    for i in list_com :
        y.append(str(int(y[-1])+1))
        print(f"컴퓨터: {y[-1]}")
    # y = [int(y[-1])+computer_turn_num] 사실 결과만 원하면 for, append를 사용해서 리스트를 만들 필요는 없고 이게더 간단함
    return y

def game() :
    print("Welcome to Arithmetic Progression Game!","\n","------------------")
    list = [0]
    while True :
        list = user_input(list)
        k = int(list[-1])
        if k >= 27:
            print("컴퓨터 승리!")
            break
        list = computer_input(list)
        k = int(list[-1])
        print("현재 숫자:", k)
        if k >= 27:
            print("유저 승리!")
            break
game()
