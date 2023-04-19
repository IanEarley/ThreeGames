from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon():
  color("lightblue")
  dot(diameter)

def inflate_balloon():
  global diameter
  diameter = diameter + 10
  draw_balloon()

  if diameter >= pop_diameter:
    clear()
    diameter = 40
    write("Pop!")

def deflate_balloon():
  global diameter
  diameter = diameter - 10

  if diameter < 40:
    diameter = 40
    exit()
  else:
    clear()
    draw_balloon()

draw_balloon()

onkey(inflate_balloon, "Up")
onkey(deflate_balloon, "Down")
listen()