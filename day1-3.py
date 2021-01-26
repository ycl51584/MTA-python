score = int(input("score?"))
if score <=100 and score >=0:
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else: 
        print("E")
else: 
    print("error")