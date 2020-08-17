#Jameson Smith 
#Cat Collector v 1.0

#imports
import addCats
import random

#list for storing the cats that are created
global cats_list
cats_list = []

#class for creating the users profile
class Cat(object):
  '''class for managing all the users cats, money and food'''
  def __init__(self,money=100,food=0):
    '''inits the money and food'''
    self.money = int(money)
    self.food = int(food)

  def add_cat(self):
    '''used for adding cats to the cats_list. Calls upon addCats.AddCats to create the cats properties and init it'''
    add_cat_input = input("Adding a cat will cost 50$ are you sure you would like to add one? (1)Yes\n")
    if self.money >= 50:
      if add_cat_input == "1": 
        global cat_name_input
        cat_name_input = input("What will you name the cat?\n")
        cats_list.append(cat_name_input)
        cat_num = (cats_list.index(cat_name_input))
        cats_list[cat_num] = addCats.AddCats()
        self.money -= 50 
    else:
       print("Not enough money\n")   

  def buy_food(self):
    '''used to add food to the users inventory'''
    food_buy_input = input("Buying 1 food will cost you 25$\nWould you like to purchase? (1)Yes\n")
    if self.money >= 25:
      if food_buy_input == "1": 
        self.money -= 25
        self.food += 1
        print("You have bought one food!")
    else:
       print("Not enough money\n")

  def get_cats(self):
    '''gets all the cats in the list and allows the user to view their status and to interact with them'''
    print("Cats:\n")
    for cats in cats_list:
      print(cats.get_name())
      cats.get_hunger()
      cats.get_pet_time()
      cats.get_mood()
    cat_select_input = input("Would you like to interact with one of these cats? (1)Yes\n")
    if cat_select_input == "1":
      cat_choice_input = input("Which one? (Type in their full name)\n")

      for cats in cats_list:
        cat_name = cats.get_name()
        if str(cat_choice_input) == str(cat_name):
          print("What would you like to do with",cat_choice_input,"?\nPet them(1)\nFeed them(2)\n")
          selection_input =input()
          if selection_input == "1":
            cats.set_pet_time()
          if selection_input == "2":
            if self.food >= 1:
              cats.set_hunger_up()
              self.food -= 1
            else:
              print("You have no food")

  def get_money_food(self):
    '''prints the users current food and money'''
    print("You have:",self.money,"$")
    print("You have:", self.food,"food")

  def set_money(self):
    '''adds money to the users account. Is triggered every second by the timer in main.py'''
    for num_of_cats in cats_list:
      self.money += 1

#random events
  def random_events_cat(self):
    '''method for triggering random events for the users cats'''
    prices = [100,150,200,250,300,350,400,450,500] #prices the cat can sell for

    #cat randomly finds food
    food_find = random.randint(0,250)
    if food_find == 250:
      print("\nRandom event!\nA cat has found food!\n")
      self.food += 1
    #cat is purchased
    cat_offer = random.randint(0,450)
    if cat_offer == 450 and len(cats_list) >= 1:
      random_cat = random.randint(0,len(cats_list)-1)
      cat_name = cats_list[random_cat].get_name()
      cat_price = str(random.choice(prices))
      print("\nRandom event!\nSomeone has bought your cat",cat_name,"for",cat_price,"$")
      cats_list.pop(random_cat)
      self.money += int(cat_price)