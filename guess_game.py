#Without using google xD
# print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!\n")
# user_name=input("Enter Your name: ")
# game_over='y'
# #loop if user want to play again
# while game_over=='y' or game_over=='Y':
#     #computer generate random number
#     import random
#     a=list(range(0,10))
#     random.shuffle(a)
#     comp=a[:3]
#     print(comp)
#     attempt=10
#     guess_count=0
#     #user have only 10 attempt  to win game
#     while attempt>=0:
#         user_input=[]
#         guess_count+=1
#         #take input from user 
#         for i in range(3):
#             num=int(input("Guess Any Number: "))
#             user_input.append(num)
#         print(f"You have {attempt} Attempt left\n")
#         #compare number
#         if user_input==comp:
#             print(f"Congratulations {user_name}\nCODE CRACKED in {guess_count} times\n")
#             break
#         elif True:
#             digit=0
#             #check how many digits are same
#             for i in range(len(comp)):
#                 for j in range(len(user_input)):
#                     if comp[i]==user_input[j]:
#                         digit+=1
#             if digit>0:
#                 if digit==1:
#                     print("One Digit same\n")
#                 elif digit==2:
#                     print("Two Digit same\n")
#                 else:
#                     print("all digit same But not in right position\n")  
#             else:
#                 print("Wrong Guess\n")
#         attempt-=1
#         if attempt<0:
#             print("Sorry !!! Try Again\n")
#     game_over=input("Play again 'Y' and 'N'\n")





#using google :-p
import random
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!\n")
game_over="Y"
while game_over=="y" or game_over=="Y":
    genrate_num=list(range(0,10))
    random.shuffle(genrate_num)
    computer_guess=genrate_num[:3]
    print(computer_guess)
    attempt=3
    guess_count=0
    while attempt>=0:
        user_input=[]
        guess_count+=1
        num=input("Enter 3 Digit number: ")
        for i in num:
            user_input.append(int(i))
        if user_input==computer_guess:
            print("Code Cracked")
            break
        else:
            help=[]
            help.clear()
            for i,digit in enumerate(computer_guess):
                if user_input[i]==digit:
                    help.append("match")
                elif digit in user_input:
                    help.append("close")
                else:
                    help.append("Wrong")
        print(help)
        print(f"You have {attempt} Attempt left\n")        
        attempt-=1
        if attempt<0:
            print("Sorry !!! Try Again\n")
    game_over=input("Play again 'Y' and 'N'\n")









