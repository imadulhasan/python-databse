from turtle import*
from polygon import*

# defining for making fuction
#speed('fastest')

for i in range (6):
    hexagone(100)
    for i in range (6):
        hexagone(50)
        circle(50)
        lt(65)
    lt(76)    

hideturtle()
mainloop()    


