from random import randint

class Actor:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.stamina = 100
    self.depression = 0
    self.damage = 2
  
  #def hello(self):
   # print "%s" % item for item in self.items())
   
  def hello(self):
   print("[", self.name,"] attacks!", sep="")
   print("    Health: ",self.health)
   print("    Stamina: ",self.stamina)
   print()

  @property
  def alive(self):
    return self.health > 0


  def attack(self, other):
    damage = randint(1,15)
    self.hello()
    print("    Damage:",damage)
    other.health -= damage
    self.stamina -= damage/2
    print()