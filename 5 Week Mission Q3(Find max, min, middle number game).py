def computer_num():
    import random
    while True :
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        if number_2 == number_1:
            number_2 = random.randint(0, 100)
            continue
        number_3 = random.randint(0, 100)
        if number_3 == number_1 or number_3 == number_2:
            number_3 = random.randint(0, 100)
            continue
        break

    max_num = 100
    min_num = 0
    num_list =[number_1, number_2, number_3]
    num_list.sort()
    max_num = num_list[2]
    mid_num = num_list[1]
    min_num = num_list[0]
    return max_num, mid_num, min_num

def userinput():
    while True :
        try :
            user_input = int(input("Please enter a number:"))
            break
        except :
            print("Please enter numeric input")
    return user_input

def guess_num() :
    max_num, mid_num, min_num = computer_num()
    n = 0
    m = []
    find_num = 0

    while True :
        if len(m) == 3:
            break
        n = n + 1
        print(f"{n}차시도")
        u = userinput()
        t = False

        for k in m :
            if u == k : # 입력값이 이미 찾은 값일 때 True
                t = True

        if t is False : # 입력값이 이미 찾은 값 중에 없을 때
            if u == max_num :
                print(f"Congraturation! {u} is Maximum.")
                m.append(max_num)
                find_num = n
                continue
            elif u == min_num :
                print(f"Congraturation! {u} is Minimum.")
                m.append(min_num)
                find_num = n
                continue
            elif u == mid_num :
                print(f"Congraturation! {u} is Middle Number.")
                m.append(mid_num)
                find_num = n
                continue
        else : # 입력값이 이미 찾은 값 중에 있을 때
            if u == max_num :
                print(f"You already find Maximum {max_num}.")
            elif u == min_num :
                print(f"You already find Minimum {min_num}.")
            else :
                print(f"You already find Middle Number {mid_num}.")

        if n == 5 :
            if find_num == 0 : # 1~4회차에서 값을 못 찾았을 때
                if min_num in m : # 이미 최소값을 찾았을 때
                    if not u == min_num : # 입력값이 최소값이 아닐 때
                        print(f"You already find Minimum {min_num}.")
                else : # 최소값을 못찾았을 때
                    if u > min_num:
                        print(f"Minimum is under {u}")
                    else:
                        print(f"Minimum is over {u}")

        if n == 10 :
            if not 5 < find_num < 10 :  # 6~9회차에서 값을 못 찾았을 때
                if max_num in m : # 1~5회차에서 이미 최대값을 찾았을 때
                    if not u == max_num : # 입력값이 최대값이 아닐 때
                        print(f"You already find Maximum {max_num}.")
                else : # 1~5회차에서도 최대값을 못 찾았을 때
                    if u > max_num :
                        print(f"Maximum is under {u}")
                    else :
                        print(f"Maximum is over {u}")

guess_num()
