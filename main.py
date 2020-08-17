#Jameson Smith 
#Cat Collector v 1.0

#imports
import cat
import threading

#start
start_input= input("\nWelcome to Cat Collector!\nPress enter key to start or press (1) to enter the tutorial\n")

#tutorial
if start_input == "1":
  print("Cat collector is a game based around creating a collection of cats\n-You start off with 100$ in your pocket\nthis is enough money to buy a cat and some food\n-When you first enter the game you will be shown this menu\n\nMain menu\n\nPress (1) to add a cat\nPress (2) to view your current cats\nPress (3) to buy more food\nPress (4) to view your money and food\n\n-You can press 1 to start and add a cat\n-Follow the on screen intructions to create your cat\n-Now that you own a cat you must make sure to feed and pet them in the view cats menu\n-You can buy food in the menu\n-If you fail to feed or pet your cat it will starve or become depressed\n-This will cause the cat to act out or die\n\n-The main object of the game is to care for and make money off of your cats\n-Each cat will make you a dollar every second\nand there will be a random chance of the cat being purchased\nwhich will make you even more money\n")
input("Press any key to begin!")

#clear console
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

#timer function for running methods on loop
def timer():
  import cat
  threading.Timer(1.0,timer).start()
  main_cats.set_money()
  main_cats.random_events_cat()
  for cats in cat.cats_list:
    cats.set_hunger_down()
    cats.set_mood()
    cats.set_pet_time_down()
    cats.rnd_events()

#create main profile
main_cats = cat.Cat()

#start timer
timer()

#main menu
while True:
  main_menu_selection = input("\nMain menu\n\nPress (1) to add a cat\nPress (2) to view your current cats\nPress (3) to buy more food\nPress (4) to view your money and food\n")
  #clear screen
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  #selections
  if main_menu_selection == "1":
    main_cats.add_cat()
  if main_menu_selection == "2":
    main_cats.get_cats()
  if main_menu_selection == "3":
    main_cats.buy_food()
  if main_menu_selection == "4":
    main_cats.get_money_food()