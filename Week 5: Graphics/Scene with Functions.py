from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 20, 70, 'pink')
    draw_cloud(canvas, 250, 50, 'purple')
    draw_tree(canvas, 40, 'green')
    draw_tree(canvas, 120, 'red')
    draw_tree(canvas, 280, 'gold')

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, leaf_color):
    canvas.create_rectangle(
        x,
        TREE_BOTTOM_Y - TRUNK_HEIGHT,
        x + TRUNK_WIDTH,
        TREE_BOTTOM_Y,
        color='brown'
    )
    mid_x = x + TRUNK_WIDTH / 2
    canvas.create_oval(
        mid_x - LEAVES_SIZE / 2,
        TREE_BOTTOM_Y - TRUNK_HEIGHT *2/3 - LEAVES_SIZE,
        mid_x + LEAVES_SIZE / 2,
        TREE_BOTTOM_Y - TRUNK_HEIGHT*2/3,
        color=leaf_color
    )

if __name__ == '__main__':
    main()
