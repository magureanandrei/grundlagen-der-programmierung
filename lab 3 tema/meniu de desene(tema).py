import turtle

t=turtle.Pen()
p=turtle.Pen()
def dreieck(latura,pen):
    for i in range(1, 4):
        pen.forward(latura)
        pen.left(120)

def quadrat(latura,pen):
    for i in range(1,5):
        pen.forward(latura)
        pen.left(90)

def rechtecke(inaltime,latime):
    for i in range(1,3):
        t.forward(latime)
        t.right(90)
        t.forward(inaltime)
        t.right(90)

def Haeuser():
    # corpul caselor
    t.penup()
    t.backward(200)
    t.pendown()
    p.penup()
    p.right(90)
    p.forward(100)
    p.left(90)
    p.pendown()
    quadrat(100, t)
    quadrat(200, p)

    # usile
    t.forward(35)
    p.forward(70)
    dreieck(30, t)
    dreieck(60, p)

    # geamuri
    t.penup()
    p.penup()
    t.left(90)
    t.forward(50)
    p.left(90)
    p.forward(100)
    t.pendown()
    p.pendown()
    t.right(90)
    p.right(90)
    t.backward(20)
    p.backward(40)
    dreieck(20, t)
    dreieck(40, p)
    t.penup()
    p.penup()
    t.forward(50)
    p.forward(100)
    t.pendown()
    p.pendown()
    dreieck(20, t)
    dreieck(40, p)
    t.penup()
    p.penup()
    t.forward(35)
    p.forward(70)
    t.left(90)
    p.left(90)
    t.forward(50)
    p.forward(100)
    t.right(90)
    p.right(90)
    t.backward(100)
    p.backward(200)
    t.pendown()
    p.pendown()
    dreieck(100, t)
    dreieck(200, p)


def Rechteck():
    t.speed(1)
    rechtecke(100,200)
    t.penup()
    t.forward(125)
    t.right(90)             #### aici repozitionez sageata pentru al doilea rechteck
    t.forward(25)
    t.pendown()
    rechtecke(50,25)
    t.reset()

def Herz():
    t.speed(1)
    t.right(90)
    t.circle(50, -180)
    t.right(180)
    t.circle(50, -180)

    t.goto(100, -150)
    t.goto(0, 0)
    t.reset()
def menu():
    return """
        1 - Rechteck
        2 - Herz
        3 - Haeuser
        0 - Exit
    """
def main():
    while True:
        print(menu())
        opt = int(input('opt= '))
        if opt == 1:
            Rechteck()
        if opt == 2:
            Herz()
        if opt == 3:
            Haeuser()
        if opt == 0:
            break

main()
