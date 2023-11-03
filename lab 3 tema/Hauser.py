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

# def main():
#     t.speed(2)
#     t.penup()
#     t.backward(200)
#     t.pendown()
#     quadrat(100)
#     t.forward(35)
#     dreieck(30)  ##usa
#     t.forward(30)
#     t.penup()
#     t.left(90)
#     t.forward(60)
#     t.pendown()
#     t.right(90)
#     dreieck(20)  ###geam 1
#     t.right(180)
#     t.penup()
#     t.forward(50)
#     t.right(180)
#     t.pendown()
#     dreieck(20)  ###geam 2
#     t.right(180)
#     t.penup()
#     t.forward(15)
#     t.right(90)
#     t.forward(40)
#     t.pendown()
#     t.right(90)
#     dreieck(100)  ###acoperis
#     ## tot ce este intre componentele casei este reorientare de sageata
#     t.penup()
#     t.right(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(200)
#     t.right(90)
#     t.forward(100)
#     t.left(90)
#     t.pendown()
#     ##casa 2
#     quadrat(200)
#     t.forward(70)
#     dreieck(60)  ##usa
#     t.forward(60)
#     t.penup()
#     t.left(90)
#     t.forward(120)
#     t.pendown()
#     t.right(90)
#     dreieck(40)  ###geam 1
#     t.right(180)
#     t.penup()
#     t.forward(100)
#     t.right(180)
#     t.pendown()
#     dreieck(40)  ###geam 2
#     t.right(180)
#     t.penup()
#     t.forward(30)
#     t.right(90)
#     t.forward(80)
#     t.pendown()
#     t.right(90)
#     dreieck(200)  ###acoperis

## tot ce este intre componentele casei este reorientare de sageata

# main()


def main():

    #corpul caselor
    t.penup()
    t.backward(200)
    t.pendown()
    p.penup()
    p.right(90)
    p.forward(100)
    p.left(90)
    p.pendown()
    quadrat(100,t)
    quadrat(200,p)

    #usile
    t.forward(35)
    p.forward(70)
    dreieck(30,t)
    dreieck(60,p)

    #geamuri
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
    dreieck(20,t)
    dreieck(40,p)
    t.penup()
    p.penup()
    t.forward(50)
    p.forward(100)
    t.pendown()
    p.pendown()
    dreieck(20,t)
    dreieck(40,p)
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
    dreieck(100,t)
    dreieck(200,p)



main()