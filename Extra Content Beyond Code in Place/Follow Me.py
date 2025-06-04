from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, 
        BALL_DIAMETER,
        'blue'
    )
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # Center the ball on the mouse
        new_x = mouse_x - BALL_DIAMETER / 2
        new_y = mouse_y - BALL_DIAMETER / 2
        canvas.moveto(ball, new_x, new_y)

        time.sleep(PAUSE_TIME)
        # Optional: print for debugging
        # print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

# No need to edit this part
if __name__ == '__main__':
    main()
