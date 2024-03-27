import turtle

MAXIMUM_ANGLE = 360.0


def create_bob():
    bob = turtle.Turtle()
    bob.color('green')
    bob.shape('turtle')
    bob.speed(1)
    return bob


def draw_square():
    bob = create_bob()

    bob.forward(100)
    bob.left(90)

    bob.forward(100)
    bob.left(90)

    bob.forward(100)
    bob.left(90)

    bob.forward(100)
    bob.left(90)


def draw_triangle():
    bob = create_bob()

    bob.forward(100)
    bob.left(120)

    bob.forward(100)
    bob.left(120)

    bob.forward(100)
    bob.left(120)


if __name__ == "__main__":

    simon_says = input("What does Simon Say?: ").lower()

    if simon_says == "square":
        draw_square()
    elif simon_says == "triangle":
        draw_triangle()
    else:
        print("Bob does not know how to draw that shape.")


