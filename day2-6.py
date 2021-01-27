score_list=[]
num=int(input('number?'))
for i in range(num):
    score=int(input('score?'))
    score_list.append(score)
    if score_list[i]<60:
        score_list[i]=60
print("high",sorted(score_list)[-1],"low",sorted(score_list)[0])

 