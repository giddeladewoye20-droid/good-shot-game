import pgzrun
from random import randint

WIDTH=500
HEIGHT=500
TITLE="PAQUETA CRISPS"

alien=Actor("alien")
msg=""

def draw():

    screen.clear()
    screen.fill("lime")

    alien.draw()
    screen.draw.text(msg,center=(400,20),fontsize=30,color="orange")

























pgzrun.go()