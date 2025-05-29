#Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. There is a gap between each wave.

from karel.stanfordkarel import *

def main():
    for _ in range(4):
        draw_wave()
        move_to_next_wave()

def draw_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    turn_right()
    put_beeper()
    turn_right()
    move()
    turn_left()

def move_to_next_wave():
    if front_is_clear():
        move()
    if front_is_clear():
        move()

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()
