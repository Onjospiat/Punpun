from Actor import *
from random import randint

p1 = Actor("Bernardo")
p2 = Actor("Eduardo")
rounds = 0
# print '%s' % item for item in p1.items())

#p1.hello()

while p1.alive and p2.alive:
  rounds += 1
  print("Round",rounds)
  #p1.hello()
  #p2.hello()
  
  turn = randint(0,1)
  
  if turn==1:
    p1.attack(p2)
    if p2.alive:
      p2.attack(p1)
      
  else:
    p2.attack(p1)
    if p1.alive:
      p1.attack(p2)
      
if p1.alive:
  print(p1.name, "venceu!")
else:
  print(p2.name, "venceu!")