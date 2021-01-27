import random
ans=random.randint(1,100)
print(ans)
guessTime=1
while True:
    guess = input("guess number?")
    if ans == int(guess):
        print("right")
        print("你猜了",guessTime,"次")
        break
        
    elif ans < int(guess):
        print('guess,lower')  
        print("wrong")
        guessTime+=1       
    else:
        print('guess,higher')
        print("wrong")
        guessTime+=1
           