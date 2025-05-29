from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    BRICKS_IN_BASE = 14 
    start_x = (CANVAS_WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH))/2 
    layer = 1 

    while BRICKS_IN_BASE > 0:
        
        for i in range(BRICKS_IN_BASE):
            create_brick(
                canvas, 
                start_x + i * BRICK_WIDTH,
                CANVAS_HEIGHT - BRICK_HEIGHT * layer, 
                'yellow'
            )
        start_x = start_x + 15
        layer = layer + 1   
        BRICKS_IN_BASE = BRICKS_IN_BASE - 1  
    
def create_brick(canvas, x1, y1, color):
    x2 = x1 + BRICK_WIDTH
    y2 = y1 + BRICK_HEIGHT

    canvas.create_rectangle(
        x1,
        y1,
        x2,
        y2,
        color,
        'black'
    )

if __name__ == '__main__':
    main()
