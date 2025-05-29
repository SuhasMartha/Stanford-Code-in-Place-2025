#The programmer wants to draw two cars, one at location (10, 10) and another at location (100, 100). When they run their program they get a "NameError" and the IDE complains that inside draw_car it doesn't know what canvas, x, or y mean.


from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas, x, y)  # pass canvas, x, y as arguments to draw_car

    x = 100
    y = 100
    draw_car(canvas, x, y)  # pass canvas, x, y as arguments to draw_car

def draw_car(canvas, x, y):  # add parameters canvas, x, y to function signature
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
