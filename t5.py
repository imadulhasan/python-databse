from turtle import*

pencolor('blue')
pensize(3)
fillcolor('black')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    
    end_fill()

mainloop()    