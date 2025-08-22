import turtle

print("----------------------------- STILL IN PROTOTYPE ------------------------------")
print("-------------------------------------------------------------------------------")

#------------------------
t = turtle.Turtle()
t.hideturtle()
#ajfhao
one = turtle.Turtle()
one.hideturtle()

two = turtle.Turtle()
two.hideturtle()

three = turtle.Turtle()
three.hideturtle()

four = turtle.Turtle()
four.hideturtle()

five = turtle.Turtle()
five.hideturtle()

six = turtle.Turtle()
six.hideturtle()

seven = turtle.Turtle()
seven.hideturtle()

eight = turtle.Turtle()
eight.hideturtle()

nine = turtle.Turtle()
nine.hideturtle()

ten = turtle.Turtle()
ten.hideturtle()

plus = turtle.Turtle()
plus.hideturtle()

minus = turtle.Turtle()
minus.hideturtle()

multiply = turtle.Turtle()
multiply.hideturtle()

divide = turtle.Turtle()
divide.hideturtle()

#------------------------

t.speed(0)
t.up()
t.width(4)
t.down()

#____Main Square____

t.up()
t.forward(-100)
t.left(90)
t.forward(15)
t.right(90)
t.down()
for i in range(2):
   t.forward(270 + 30)
   t.right(45)
   t.forward(10)
   t.right(45)
   t.forward(280)
   t.right(45)
   t.forward(10)
   t.right(45)

t.width(2)
t.forward(210 + 10)
t.right(90)
t.up()
t.forward(15)
t.down()
t.forward(260)

#-------------------------------------------------#
one.up()
one.width(3)
one.speed(0)
one.down()

two.up()
two.width(3)
two.speed(0)
two.down()

three.up()
three.width(3)
three.speed(0)
three.down()

four.up()
four.width(3)
four.speed(0)
four.down()

five.up()
five.width(3)
five.speed(0)
five.down()

six.up()
six.width(3)
six.speed(0)
six.down()

seven.up()
seven.width(3)
seven.speed(0)
seven.down()

eight.up()
eight.width(3)
eight.speed(0)
eight.down()


nine.up()
nine.width(3)
nine.speed(0)
nine.down()


ten.up()
ten.width(3)
ten.speed(0)
ten.down()

plus.up()
plus.width(3)
plus.speed(0)
plus.down()

minus.up()
minus.width(3)
minus.speed(0)
minus.down()

multiply.up()
multiply.width(3)
multiply.speed(0)
multiply.down()

divide.up()
divide.width(3)
divide.speed(0)
divide.down()

#-------------------------------------------------#

#-------------------SCREEN SAVES-------------------#

l = turtle.Turtle()
l.speed(0)
l.width(5)
l.hideturtle()
l.up()
l.goto(-108.0, 125.0)
l.down()

def letter_one():
   l.write("1",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_two():
   l.write("2",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_three():
   l.write("3",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   l.down()

def letter_four():
   l.write("4",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_five():
   l.write("5",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_six():
   l.write("6",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_seven():
   l.write("7",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_eight():
   l.write("8",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_nine():
   l.write("9",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_ten():
   l.write("0",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_plus():
   l.write("+",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_minus():
   l.write("-",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_multiply():
   l.write("x",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_divide():
   l.write("÷",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

#-------------------SCREEN SAVES-------------------#

#-------------------KEYBOARD DEFS-------------------#  
   
#-------------- ONE --------------#
one.up()
one.forward(-90)
one.down()
for i in range(4):
    one.forward(50)
    one.right(45)
    one.forward(5)
    one.right(45)

one.up()
one.right(90)
one.forward(50)
one.left(90)
one.forward(17)
one.write("1",font=("Courier",25,'bold'))
one.hideturtle()
#-------------- ONE --------------#

#-------------- TWO --------------#
two.up()
two.forward(-20)
two.down()
for i in range(4):
    two.forward(50)
    two.right(45)
    two.forward(5)
    two.right(45)

two.up()
two.right(90)
two.forward(50)
two.left(90)
two.forward(17)
two.write("2",font=("Courier",25,'bold'))
two.hideturtle()
#-------------- TWO --------------#

#-------------- THREE --------------#
three.up()
three.forward(50)
three.down()
for i in range(4):
    three.forward(50)
    three.right(45)
    three.forward(5)
    three.right(45)

three.up()
three.right(90)
three.forward(50)
three.left(90)
three.forward(17)
three.write("3",font=("Courier",25,'bold'))
three.hideturtle()
#-------------- THREE --------------#

#-------------- FOUR --------------#
four.up()
four.forward(-90)
four.right(90)
four.forward(70-3)
four.right(-90)
four.down()
for i in range(4):
    four.forward(50)
    four.right(45)
    four.forward(5)
    four.right(45)

four.up()
four.right(90)
four.forward(50)
four.left(90)
four.forward(17)
four.write("4",font=("Courier",25,'bold'))
four.hideturtle()
#-------------- FOUR --------------#

#-------------- FIVE --------------#
five.up()
five.forward(-20)
five.right(90)
five.forward(70-3)
five.right(-90)
five.down()
for i in range(4):
    five.forward(50)
    five.right(45)
    five.forward(5)
    five.right(45)

five.up()
five.right(90)
five.forward(50)
five.left(90)
five.forward(17)
five.write("5",font=("Courier",25,'bold'))
five.hideturtle()
#-------------- FIVE --------------#

#-------------- SIX --------------#
six.up()
six.forward(50)
six.right(90)
six.forward(70-3)
six.right(-90)
six.down()
for i in range(4):
    six.forward(50)
    six.right(45)
    six.forward(5)
    six.right(45)

six.up()
six.right(90)
six.forward(50)
six.left(90)
six.forward(17)
six.write("6",font=("Courier",25,'bold'))
six.hideturtle()
#-------------- SIX --------------#

#-------------- SEVEN --------------#
seven.up()
seven.forward(-90)
seven.right(90)
seven.forward(140-3)
seven.right(-90)
seven.down()
for i in range(4):
    seven.forward(50)
    seven.right(45)
    seven.forward(5)
    seven.right(45)

seven.up()
seven.right(90)
seven.forward(50)
seven.left(90)
seven.forward(17)
seven.write("7",font=("Courier",25,'bold'))
seven.hideturtle()
#-------------- SEVEN --------------#

#-------------- EIGHT --------------#
eight.up()
eight.forward(-20)
eight.right(90)
eight.forward(140-3)
eight.right(-90)
eight.down()
for i in range(4):
    eight.forward(50)
    eight.right(45)
    eight.forward(5)
    eight.right(45)

eight.up()
eight.right(90)
eight.forward(50)
eight.left(90)
eight.forward(17)
eight.write("8",font=("Courier",25,'bold'))
eight.hideturtle()
#-------------- EIGHT --------------#

#-------------- NINE --------------#
nine.up()
nine.forward(50)
nine.right(90)
nine.forward(140-3)
nine.right(-90)
nine.down()
for i in range(4):
    nine.forward(50)
    nine.right(45)
    nine.forward(5)
    nine.right(45)

nine.up()
nine.right(90)
nine.forward(50)
nine.left(90)
nine.forward(17)
nine.write("9",font=("Courier",25,'bold'))
nine.hideturtle()
#-------------- NINE --------------#

#-------------- TEN --------------#
ten.up()
ten.forward(-20)
ten.right(90)
ten.forward(210-3)
ten.right(-90)
ten.down()
for i in range(4):
    ten.forward(50)
    ten.right(45)
    ten.forward(5)
    ten.right(45)

ten.up()
ten.right(90)
ten.forward(50)
ten.left(90)
ten.forward(17)
ten.write("0",font=("Courier",25,'bold'))
ten.hideturtle()
#-------------- TEN --------------#

#-------------- PLUS --------------#
plus.up()
plus.forward(140)
plus.down()
for i in range(4):
    plus.forward(50)
    plus.right(45)
    plus.forward(5)
    plus.right(45)

plus.up()
plus.right(90)
plus.forward(50)
plus.left(90)
plus.forward(17)
plus.write("+",font=("Courier",25,'bold'))
plus.hideturtle()
#-------------- PLUS --------------#

#-------------- MINUS --------------#
minus.up()
minus.forward(140)
minus.right(90)
minus.forward(70-3)
minus.right(-90)
minus.down()
for i in range(4):
    minus.forward(50)
    minus.right(45)
    minus.forward(5)
    minus.right(45)

minus.up()
minus.right(90)
minus.forward(50)
minus.left(90)
minus.forward(17)
minus.write("-",font=("Courier",25,'bold'))
minus.hideturtle()
#-------------- MINUS --------------#

#-------------- MULTIPLE --------------#
multiply.up()
multiply.forward(140)
multiply.right(90)
multiply.forward(140-3)
multiply.right(-90)
multiply.down()
for i in range(4):
    multiply.forward(50)
    multiply.right(45)
    multiply.forward(5)
    multiply.right(45)

multiply.up()
multiply.right(90)
multiply.forward(50)
multiply.left(90)
multiply.forward(17)
multiply.write("×",font=("Courier",25,'bold'))
multiply.hideturtle()
#-------------- MULTIPLE --------------#

#-------------- DIVIDE --------------#
divide.up()
divide.forward(140)
divide.right(90)
divide.forward(210-3)
divide.right(-90)
divide.down()
for i in range(4):
    divide.forward(50)
    divide.right(45)
    divide.forward(5)
    divide.right(45)

divide.up()
divide.right(90)
divide.forward(50)
divide.left(90)
divide.forward(17)
divide.write("÷",font=("Courier",25,'bold'))
divide.hideturtle()
#-------------- DIVIDE --------------#

#-------------------KEYBOARD DEFS-------------------#  

print("U can write now :) ")

print("-------------------------------------------------------------------------------")

def check_button(x,y):
      # ONE
   if (x > -94 and x < -36 and y > -58 and y < -1):
        print("1")
        letter_one() 
   
      # TWO
   if (x > -24 and x < 34 and y > -58 and y < -1):
        print("2")
        letter_two()  
   
      # THREE
   if (x > 46 and x < 105 and y > -58 and y < -1):
        print("3")
        letter_three()
      
      # FOUR
   if (x > -94 and x < -36 and y > -124 and y < -67):
        print("4")
        letter_four()
   
      # FIVE
   if (x > -24 and x < 34 and y > -124 and y < -67):
        print("5")
        letter_five()
   
      # SIX
   if (x > 46 and x < 105 and y > -124 and y < -67):
        print("6")
        letter_six()
        
      # SEVEN
   if (x > -94 and x < -36 and y > -197 and y < -137):
        print("7")
        letter_seven()
        
      # EIGHT
   if (x > -24 and x < 34 and y > -197 and y < -137):
        print("8")
        letter_eight()
        
      # NINE
   if (x > 46 and x < 105 and y > -197 and y < -137):
        print("9")
        letter_nine()

      # TEN
   if (x > -24 and x < 34 and y > -265 and y < -207):
        print("0")
        letter_ten()

      # PLUS
   if (x > 136 and x < 195 and y > -58 and y < -1):
        print("+")
        letter_plus()

      # MINUS
   if (x > 136 and x < 195 and y > -124 and y < -67):
        print("-")
        letter_minus()

      # MULTIPLY
   if (x > 136 and x < 195 and y > -197 and y < -137):
        print("*")
        letter_multiply()

      # DIVIDE
   if (x > 136 and x < 195 and y > -265 and y < -207):
        print("÷")
        letter_divide()

print("The numbers u have wrote till now are:")

def get_mouse_coords(x,y):
   print(x,y)

#turtle.onscreenclick(get_mouse_coords)

turtle.onscreenclick(check_button)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^KEYBOARD^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#_________SCREEN TIME__________#