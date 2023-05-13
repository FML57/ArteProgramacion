from random import *
from turtle import *
from freegames import path

car = path('car.gif')
#Change tiles(numbers) to a list of letters
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:32] * 2
shuffle(letters)
state = {'mark': None}
hide = [True] * 64
taps=0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap. Counts the number of taps."
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Center the letter on the tile
        x += 25 - textwidth(letters[mark], font=('Arial', 30, 'normal')) / 2
        goto(x, y)
        color('black')
        write(letters[mark], font=('Arial', 30, 'normal'))

    update()

    # Check if the game is over when all letters are revealed
    if all(hide) == False:
        ontimer(draw, 100)
    else:
        print("Game over! You took", taps, "taps.")

shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()