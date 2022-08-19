s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

correct_answer = [3,2,4,2,5,2,4,3,1,2]

def userinput(x):
    l_name = []
    l_sub = []
    for i in x:
        find_comma = i.find(",")
        name = i[:find_comma]
        l_name.append(name)
        sub = i[find_comma + 1:]
        list_sub = list(sub)
        l_sub.append(list_sub)
    return l_name, l_sub

def test_grading(x, y) :
    name_score= []
    g_name, g_sub = userinput(x)

    for m in range(0, len(g_sub)) : # 제출 답안 갯수
        count = 0
        for n in range(0, len(y)) : # 1~10번 답안 비교
            if int(g_sub[m][n]) == int(y[n]) :
                count += 10
        name_score.append([str(count), g_name[m]])
    return name_score

def raking(x) :
    x.sort(reverse=True)
    for a in range(0, len(x)):
        print(f'학생:{x[a][1]} 점수:{x[a][0]}점 {a+1}등')


name_score = test_grading(s,correct_answer)
raking(name_score)
