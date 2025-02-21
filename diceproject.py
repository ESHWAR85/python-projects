import random
while True:
 choices=["rock","paper","sci"]
 computer=random.choice(choices)
 player=None
 while player not in choices:
     player=input(" rock , paper , sci :").lower()
     if computer==player:
         print("computer",computer)
         print("player",player)
         print("tie")
     elif computer=="rock":
         if player=="paper":
            print("computer",computer)
            print("player",player)
            print("u won")  
         if player=="sci":
           print("computer",computer)
           print("player",player)
           print("u loser")
     elif computer=="paper":
         if player=="rock":
           print("computer",computer)
           print("player",player)
           print("u loose")  
         if player=="sci":
            print("computer",computer)
            print("player",player)
            print("u won")
     elif computer=="sci":
         if player=="rock":
            print("computer",computer)
            print("player",player)
            print("u won")  
         if player=="paper":
            print("computer",computer)
            print("player",player)
            print("u loose")
 play=input("if u want to play /yes(or)no: ")
 if play=="no":
     break
  
print("bye")            

                            

