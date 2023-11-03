import turtle

t=turtle.Pen()


def rechtecke(inaltime,latime):
    for i in range(1,3):
        t.forward(latime)
        t.right(90)
        t.forward(inaltime)
        t.right(90)


def main():

    t.speed(1)
    rechtecke(100,200)
    t.penup()
    t.forward(125)
    t.right(90)             #### aici repozitionez sageata pentru al doilea rechteck
    t.forward(25)
    t.pendown()
    rechtecke(50,25)


main()