from turtle import *

def greeting (n):
  print("Hello " + n)

name = "Emily"

greeting(name)

#part 2


def move_and_turn (d, a):
  forward(d)
  right(a)

move_and_turn(100, 90)
move_and_turn(30, 200)