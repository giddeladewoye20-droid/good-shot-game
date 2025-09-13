import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="PAQUETA CRISPS"

alien=Actor("alien")
alien.pos=250,250
score=0
msg=""

def draw():

    screen.clear()
    screen.fill("lime")

    alien.draw()
    screen.draw.text(msg,center=(250,250),fontsize=30,color="purple")
def on_mouse_down(pos): 
    global msg
    global score
    if alien.collidepoint(pos):
        alien.pos=random.randint(0,500), random.randint(0,500)
        score= score + 1
        msg="You have hit the Alien!You now have " + str (score)+"points"
        
    else:
        score= score - 1
        msg="You have not hit the Alien! You now have"+ str(score) + "points"
       






pgzrun.go()