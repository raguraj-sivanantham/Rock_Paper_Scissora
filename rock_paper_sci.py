items=["ROCK","PAPER","SCISSOR"]
import time
import random
print("NOTE : TURN ON YOUR CAPS LOCK.")
def game():
    user_point=0
    machine_point=0
    for i in range(5):
        print("3",end=" ")
        time.sleep(1)
        print("2",end=" ")
        time.sleep(1)
        print("1",end=" ")
        memory=random.choice(items)
        user=input("ROCK or PAPER or SCISSOR : ")
        if memory==user:
            print("This is Draw")
        elif memory=="ROCK" and user in["SCISSOR","PAPER"]:
            if user=="SCISSOR":
                print("Computer Win!! ")
                machine_point=machine_point+1
            else:
                print("You Win !!")
                user_point=user_point+1
                
        elif memory=="PAPER" and user in["ROCK","SCISSOR"]:
            if user=="ROCK":
                print("Computer Win !!")
                machine_point=machine_point+1
            else:
                print("You Win !!")
                user_point=user_point+1
        elif memory=="SCISSOR" and user in["ROCK","PAPER"]:
            if user=="PAPER":
                print("Computer Win !!")
                machine_point=machine_point+1
            else:
                print("You Win !!")
                user_point=user_point+1

    if user_point==machine_point:
        print("Draw Match")
    elif user_point > machine_point:
        print("Winner : YOU. Points : ",user_point)
    else:
        print("Winner : COMPUTER . Points : ",machine_point)
                        
game()
print("-"*10)
check=input("Do you want to play again [YES,NO] : ")
while check=="YES":
    game()
    print("-"*10)
    check=input("Do you want to play again [YES,NO] : ")
print("---END GAME---")

