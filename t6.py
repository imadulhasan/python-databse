from turtle import*

s = Screen()
s.setup(1000,700)
color = ['purple','blue']
pencolor('green')
pensize(6)
for i in range(6,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(color[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()