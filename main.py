#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import curses
import subprocess
import os

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(10, 10, "Hit 'q' to quit")
stdscr.refresh()

PATH = os.path.dirname(os.path.realpath(__file__))
SOUNDS_MAP = {
    ord('o'): os.path.join(PATH, 'sounds/OuYeah.mp3'),
    ord('f'): os.path.join(PATH, 'sounds/fail.mp3'),
    ord('s'): os.path.join(PATH, 'sounds/success.mp3'),
}

height, width = stdscr.getmaxyx()

for i in range(width):
    stdscr.addstr(0, i, "#")
    stdscr.addstr(height - 2, i, "#")

for i in range(height - 2):
    stdscr.addstr(i, 0, "#")
    stdscr.addstr(i, width-1, "#")

key = ''
while key != ord('q'):
    key = stdscr.getch()
    if key in SOUNDS_MAP.keys():
        sound = SOUNDS_MAP[key]
        stdscr.addstr(20, 20, "Play Sound: {}".format(sound))
        subprocess.Popen(['mpg123', '-q', sound]).wait()
        stdscr.refresh()
    elif key == curses.KEY_UP:
        stdscr.addstr(2, 20, "Up")
    elif key == curses.KEY_DOWN:
        stdscr.addstr(3, 20, "Down")
    else:
        stdscr.refresh()

curses.endwin()

if __name__ == '__main__':
    cmd = Command(arguments=sys.argv[1:])
