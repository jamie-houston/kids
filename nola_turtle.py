
import turtle

def draw_letter_n(nola, color):
  nola.color(color)
  nola.forward(30)
  nola.right(135)
  nola.forward(40)
  nola.left(135)
  nola.forward(30)


def draw_letter_o(nola, color):
  nola.color(color)
  nola.circle(15)
  
def draw_letter_l(nola, color):
  nola.color(color)
  nola.left(90)
  nola.forward(30)
  nola.left(180)
  nola.forward(30)
  nola.left(90)
  nola.forward(15)
  
  
  
def draw_letter_a(nola, color):
  nola.color(color)
  nola.width(3)
  nola.left(80)
  nola.forward(36)
  nola.right(150)
  nola.forward(20)
  nola.right(110)
  nola.forward(10)
  nola.right(180)
  nola.forward(10)
  nola.right(75)
  nola.forward(15)
  
def draw_nola(nola):
  nola.left(90)

  draw_letter_n(nola, "blue")
  
  nola.penup()
  
  nola.right(160)
  nola.forward(20)
  nola.pendown()
  
  draw_letter_o(nola, "green")
  
  nola.penup()
  
  nola.left(60)
  nola.forward(40)
  nola.left(10)
  nola.pendown()
  
  draw_letter_l(nola, "red")
  
  nola.penup()
  nola.forward(10)
  nola.pendown()
  
  draw_letter_a(nola, "gold")

def draw_letter_p(nola, color):
  nola.color(color)
  nola.left(90)
  nola.pendown()
  nola.forward(35)
  nola.right(90)
  nola.circle(20,180)
  nola.left(90)
  nola.forward(50)
  nola.left(90)
  nola.penup()
  nola.forward(20)
  nola.pendown()
  
def draw_letter_r(nola, color):
  nola.color(color)
  nola.forward(30)
  nola.right(90)
  nola.circle(15, 180)
  nola.left(90)
  nola.forward(30)
  nola.left(35)
  nola.forward(35)
  
def draw_letter_k(nola, color):
  nola.color(color)
  nola.forward(50)
  nola.right(180)
  nola.forward(25)
  nola.left(140)
  nola.forward(35)
  nola.right(180)
  nola.forward(35)
  nola.left(90)
  nola.forward(35)

def draw_letter_e(nola, color):
  nola.color(color)
  nola.forward(50)
  nola.right(90)
  nola.forward(10)
  nola.right(180)
  nola.forward(10)
  nola.left(90)
  nola.forward(25)
  nola.left(90)
  nola.forward(10)
  nola.right(180)
  nola.forward(10)
  nola.left(90)
  nola.forward(25)
  nola.left(90)
  nola.forward(10)
  
def draw_parker(nola):
  draw_letter_p(nola, "red")
  draw_letter_a(nola, "orange")
  nola.penup()
  nola.left(80)
  nola.forward(10)
  nola.left(90)
  nola.pendown()
  draw_letter_r(nola, "green")
  nola.left(50)
  nola.penup()
  nola.forward(10)
  nola.left(90)
  nola.pendown()
  draw_letter_k(nola, "blue")
  nola.penup()
  nola.left(20)
  nola.forward(10)
  nola.left(90)
  nola.pendown()
  draw_letter_e(nola, "purple")
  
nola = turtle.Turtle()

nola.shape("turtle")

nola.speed(3)
#draw_nola(nola)
draw_parker(nola)
#nola.left(90)
#draw_letter_k(nola, "green")
