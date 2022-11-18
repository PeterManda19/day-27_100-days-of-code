import os, time, random


print("⚔️   Character Builder ")
print("⚔️")
print()
print("Everytime you key in your response press enter.")


def rollDice(num):
    return random.randint(1,num)


def userName():
  while True:
    print()
    name = input("Name Your Legend: ")
  
    if name.isnumeric() == True:
      print("I am expecting a name not just numbers.")
      continue
    print(name.capitalize(),"the Marvelous")
    print()
    break


def charType():
  charTypeList = ["human", "elf", "wiard", "orc"]
  while True:
    print()
    type = input("Character Type (Human, Elf, Wiard, Orc): ")
  
    if type.lower() not in charTypeList:
      print("Please enter one of the options in enclosed in brackets.")
      continue
    print(type.capitalize())
    print()
    break


def displayChar():
  
  quitList = ["y","yes", 'quit', 'exit']
  exit = ""
  while exit.lower() not in quitList:
    userName()
    charType()
    health = ((rollDice(7) * rollDice(13)) / 2) +12
    strength = ((rollDice(7) * rollDice(13)) / 2) +12
    print("HEALTH:",health)
    print("STRENGTH:",strength)
    print()
   
    time.sleep(3)
    os.system("clear")
   
    print("To exit enter 'y' or 'yes' or 'quit' or 'exit'")
    exit = input("Would like to exit the game? ")  
    
      
def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to generate health stats.""")
    print()
    continue


if __name__=="__main__":
  displayChar()
  endGame()