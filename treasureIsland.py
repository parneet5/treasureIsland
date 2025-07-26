print('''    
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                                            
                         
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%_________
''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

print("You're at a cross road. Where do you want to go?")
     
user_Choice = input("Type left or right \n").lower()

if user_Choice == "left":
  print("You have come to a lake.There is an island in the middle of the lake.")
  choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

  if choice2 == "wait":
    print("You have arrived at the island unharmed.\n Which door you want to enter into?")
    choice3 = input('Input "red" for a red door, "blue" for a blue door, "yellow" for a yellow door\n').lower()

    if choice3 == "red":
      print("You entered a fire room.\n You are burnt alive. Game is Over")

    elif choice3 == "blue":
      print("You entered a room of beasts.\n You are eaten alive. Game is Over")

    elif choice3 == "yellow":
      print("Congratulations!, You found the treasue. You Won")

    else:
      print("You have entered a wong door. Game Over")
  
  else:
    print("You are attacked by a trout. Your Game is Over.")

else:
  print("Oops!, You fall into a hole.\nGame Over")
  



 




