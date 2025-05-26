from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    while front_is_clear() and no_beepers_present():
        move()
    put_beeper()
    turn_back()

    while front_is_clear() and no_beepers_present():
        move()
    put_beeper()
    turn_back()
    
    while no_beepers_present():
        cycle_A()
    
    pick_beeper()
    turn_back()
    turn_left()
    turn_left()
    if facing_west():
        turn_left()
        turn_left()

def turn_back():
    turn_left()
    turn_left()
    move()

def cycle_A():

    while front_is_clear() and no_beepers_present():
        move()
    pick_beeper()
    turn_back()
    put_beeper()
    move()

if __name__ == '__main__':
    main()
