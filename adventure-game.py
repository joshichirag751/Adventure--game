start = input("do you want to play game? yes/no").lower()
if start == "yes":
  print("ok! you are in start position")
  x = input("where do you want to go ? right / left")
  if x =="right":
    option = input("correct or incorrect ?")
    if option == "correct":
      print ("you are on right track ")
      path= input ("you see car and plane how do you want to go by car/plane ?")

      if path =="car":
        print("you do not know how to drive car")
      else:
        print("you won!!!")
    else :
      print("you took aimless walk to right and slip on a patch of ice you are unable to continue . its game over")

  elif x =="left":
    print("correct you encounter a monster  ")
    move=input("do you want to attack / run ?")
    if move == "attack":
      print("that wasnt best idea")
    else :
      print("excellent! you got away")
elif start =="no":
  print("bit sad")
else:
  print("invalid")