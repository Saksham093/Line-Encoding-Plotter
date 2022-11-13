import turtle
import tkinter as tk


class NRZ_I:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        t.sety(self.logic_high)  # assume previous signal is a high
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.forward(self.distance)

    def one(self):
        posx, posy = t.pos()
        if self.logic_low - 1 < posy < self.logic_low + 1:
            t.sety(self.logic_high)
        elif self.logic_high - 1 < posy < self.logic_high + 1:
            t.sety(self.logic_low)
        t.forward(self.distance)
        print(posy)


class NRZ_L:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)


class RZ:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_low)
        t.forward(self.distance)
        t.sety(self.base)
        setTurtle(*invisiline)
        t.write('0', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_high)
        t.forward(self.distance)
        t.sety(self.base)
        setTurtle(*invisiline)
        t.write('1', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)


class Manchester:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)
        setTurtle(*invisiline)
        t.write('0', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.sety(self.logic_low)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)
        t.sety(self.logic_high)
        setTurtle(*invisiline)
        t.write('1', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)


class diff_Manchester:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        prev_num = 2  # assume previous number is pattern 2
        for i in self.signal:
            if i == '0':
                self.pattern(prev_num, '0')
            elif i == '1':
                num = 1 if prev_num == 2 else 2
                self.pattern(num, '1')
                prev_num = num

    def pattern(self, num, write):
        if num == 1:
            t.sety(self.logic_high)
            t.forward(self.distance)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.sety(self.logic_low)
            t.forward(self.distance)
        elif num == 2:
            t.sety(self.logic_low)
            t.forward(self.distance)
            t.sety(self.logic_high)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.forward(self.distance)


def drawAxes():
    def drawLineAndBack(distance):
        for i in range(distance // 50):
            t.forward(50)
            t.dot(5)
        t.backward(distance)

    t.hideturtle()
    t.speed('fastest')
    t.setx(-len_X // 2 + 100)
    drawLineAndBack(len_X)
    t.rt(90)
    drawLineAndBack(100)
    t.rt(180)
    drawLineAndBack(100)
    t.rt(90)


def setTurtle(size, colour, speed, visibility):
    t.pensize(size)
    t.pencolor(colour)
    t.speed(speed)
    if not visibility:
        t.hideturtle()


print('|--------------------Line Code Simulator--------------------|')

# Condition for the Input of the Signal...
while True:
    signal = str(input('Input Signal to be Plotted (1s and 0s) : '))
    ls = map(lambda x: x in {'0', '1'}, signal)

    if False in ls:
        print("\nInvalid Input Try Again.\n")
        continue
    
    break


# To avoid Error if Encoding not in the list...
print('\nEncode in Format:\n1. NRZ-I\n2. NRZ-L\n3. RZ\n4. Manchester\n5. Diff Manchester ...\n')
while True:
    encoding = str(input("\nEnter Int Value from the List : "))
    if encoding not in ['1', '2', '3', '4', '5']:
        print("\nInvalid Input Type...Retry")
        continue

    break

root = tk.Tk()
root.title('Signal Graph')
root.geometry('1000x300')
cv = turtle.ScrolledCanvas(root, width=1000)  # turn Canvas to ScrolledCanvas if signals long
cv.pack()

len_X, len_Y = 200*len(signal), 350
default_settings = (2, 'red', 'slowest', False)
invisiline = (1, 'black', 'fastest', False)
map = {'1': NRZ_I(signal), '2': NRZ_L(signal), '3': RZ(signal), '4': Manchester(signal),
       '5': diff_Manchester(signal)}

screen = turtle.TurtleScreen(cv)
screen.screensize(len_X, len_Y)
t = turtle.RawTurtle(screen)

drawAxes()
setTurtle(*default_settings)

print('\nDrawing Signal ...')
map[encoding].draw()

root.mainloop()