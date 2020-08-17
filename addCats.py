#Jameson Smith 
#Cat Collector v 1.0

#imports
import random
import cat

#class to add cats to the users profile and modify them
class AddCats(object):
  '''Class for adding cats to the collection and setting their attributes'''
  def __init__(self,name="",hunger=500,mood="",pet_time =500):
    '''init cats and therir attributes'''
    self.name = name
    self.hunger = hunger
    self.mood = mood  
    self.pet_time = pet_time
    #auto sets the cats name 
    AddCats.set_name(self)

  #setters   
  def set_name(self):
    '''method for setting the cats name'''
    self.name = cat.cat_name_input
  
  def set_hunger_down(self):
    '''method for lowering the cats hunger'''
    self.hunger -= 1
    if self.hunger == 0:
      cat.cats_list.remove(self)
      print(self.name,"has starved")

  def set_hunger_up(self):
    '''method for raising the cats hunger'''
    self.hunger += 200
    print(self.name,"eats the food and loves it!")

  def set_pet_time_down(self):
    self.pet_time -= 1
    if self.pet_time == 0:
      cat.cats_list.remove(self)
      print(self.name,"has run away because he was not getting attention")

  def set_mood(self):
    '''method for setting the cats mood'''
    #different cat moods based off of hunger + time since last pet
    if self.hunger > 250:
      self.mood = "Full"
    if self.hunger <= 250:
      self.mood = "Peckish"
    if self.hunger <= 100:
      self.mood = "Hungry"
    if self.hunger <= 50:
      self.mood = "Starving"
    if self.pet_time > 249:
      self.mood += " and Happy"
    if self.pet_time <= 249 and self.pet_time > 100:
      self.mood += " and unhappy"
    if self.pet_time <= 100 and self.pet_time > 50:
      self.mood += " and sad"
    if self.pet_time <= 50:
      self.mood += " and depressed"

  def set_pet_time(self):
    '''method for raising the cats pet timer'''
    self.pet_time += 200
    print(self.name,"purrs!")

  #getters
  def get_name(self):
    '''method for returning the cats name'''
    return self.name

  def get_hunger(self):
    '''method for returning the cats hunger'''
    print("  Hunger:",self.hunger)
  
  def get_mood(self):
    '''method for returning the cats mood'''
    print("  Mood:",self.mood)
  
  def get_pet_time(self):
    '''method for returning the cats pet timer'''
    print("  Needs a pet in:",self.pet_time,"seconds")

  #random events
  def rnd_events(self):
    '''method for triggering random events based off of cat attributes'''
    #cat can randomly bite another cat
    if self.hunger <= 50: 
      hunger_random_int = random.randint(0,100)
      if hunger_random_int == 100:
        random_cat = random.randint(0,len(cat.cats_list)-1)
        cat.cats_list.pop(random_cat)
        print("\nRandom event!\n",self.get_name(),"has biten and killed a cat because he was too hungry\n")
    #cat can randomly run away
    if self.pet_time <= 50:
      angry_random_int = random.randint(0,100)
      if angry_random_int == 100:
        random_cat = random.randint(0,len(cat.cats_list)-1)
        cat.cats_list.pop(random_cat)
        print("\nRandom event!\n",self.get_name(),"has biten and killed a cat because he was negelected\n")
    #cat can randomly throw up half of it's food
    throw_up = random.randint(0,500)
    if throw_up == 500 and len(cat.cats_list) >= 1:
      print("\nRandom event!\n",self.name,"has thrown up and lost half of his hunger!")
      self.hunger = self.hunger//2