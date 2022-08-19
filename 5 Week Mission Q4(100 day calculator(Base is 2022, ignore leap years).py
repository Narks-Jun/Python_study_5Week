
def userinput() :
    while True :
        try :
            user_input = input("날짜를 입력하세요. ex)20020304 :")
            if len(user_input) != 8 :
                print("년월일 포함 8자리로 입력해주세요")
                continue
            year = int(user_input[:4])
            month = int(user_input[4:6])
            day = int(user_input[6:])
            break
        except :
            print("Please enter numeric input.")
    return year, month, day

def is_month_change(x, y, z) : # 30 or 31일이 넘으면 True값 반환
    a = [i for i in range(1, 13)]
    b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y in a :
        day_in_month = b[a.index(y)]
    if z > day_in_month:
        return True
    else:
        return False

def calender_2022(x, y, z) : # 윤년을 고려하지 않은 달력
    a = [i for i in range(1, 13)]
    b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y in a :
        for i in range(0, a.index(y)) :
            z = z + b[i]
    day_of_week = ["월", "화", "수", "목", "금", "토", "일"]
    # jan_1st = day_of_week[5]
    find_day = (x - 2022 + 5 + z - 1) % 7
    d = day_of_week[find_day]
    return d

def calculate(x, y, z) : # 100일 계산기
    for i in range(100) :
        z += 1 # 날짜에 +1씩 더함
        if is_month_change(x, y, z) : # 30 or 31 이 넘으면 월+1
            z = 1
            y += 1
            if y > 12 : # 12월이 넘으면 연+1
                y = 1
                x += 1
    return x, y, z

year, month, day = userinput()
input_day = (calender_2022(year, month, day))
a, b, c = calculate(year, month, day)
d = (calender_2022(a, b, c))
print(f"{year}년{month}월{day}일 {input_day}요일부터 100일 뒤는 {a}년{b}월{c}일 {d}요일")
