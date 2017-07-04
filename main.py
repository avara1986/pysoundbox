#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import curses
import os
import subprocess

PATH = os.path.dirname(os.path.realpath(__file__))

SCREEN = curses.initscr()

curses.noecho()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
"""
for i in range(0, curses.COLORS):
    curses.init_pair(i, i, -1)
"""

class PySoundBox(object):
    SOUNDS_MAP = {
        ord('o'): os.path.join(PATH, 'sounds/OuYeah.mp3'),
        ord('f'): os.path.join(PATH, 'sounds/fail.mp3'),
        ord('s'): os.path.join(PATH, 'sounds/success.mp3'),
        ord('w'): os.path.join(PATH, 'sounds/WhoLetTheDogsOut.mp3'),
        ord('F'): os.path.join(PATH, 'sounds/Fatality.mp3'),
        ord('h'): os.path.join(PATH, 'sounds/Hadouken.mp3'),
    }
    _COLOR_RED = 1
    _COLOR_GREEN = 2
    _COLOR_BLUE = 4

    screen = None

    key_exit = ord('q')

    def __init__(self):
        self.screen = SCREEN
        self.sound_box()
        self.draw_window()
        self.add_title("Welcome to PySoundBox")
        self.add_paragraph("Press keys to play sounds. Hit 'q' to quit")
        self.loop()
        curses.endwin()


    def add_title(self, title):
        self.screen.addstr(0, 10, title, curses.A_BOLD)

    def add_paragraph(self, paragraph):
        self.screen.addstr(10, 10, paragraph, curses.A_DIM)

    def draw_window(self):
        self.screen.border(0)

    def sound_box(self):
        self._create_pad()
        self._make_textboxes()

    def _create_pad(self):
        self.PAD_WIDTH = 400
        self.PAD_HEIGHT = 10000
        """ Creates a big self.pad to place the textboxes in. """
        self.pad = curses.newpad(self.PAD_HEIGHT, self.PAD_WIDTH)
        self.pad.box()

    def _make_textboxes(self):
        """ Build the textboxes in the pad center and put them in the
            horizontal middle of the pad. """
        # Get the actual screensize.
        self.TEXTBOX_WIDTH = 50
        self.TEXTBOX_HEIGHT = 6

        maxy, maxx = self.screen.getmaxyx()

        windows = []
        i = 1
        window = self.pad.derwin(self.TEXTBOX_HEIGHT,
                self.TEXTBOX_WIDTH, i, self.PAD_WIDTH//2-self.TEXTBOX_WIDTH//2)

        window.box()
        window.addstr(4, 4, 'test')

    def loop(self):
        key = ''
        while key != ord('q'):
            key = self.screen.getch()
            if key in self.SOUNDS_MAP.keys():
                sound = self.SOUNDS_MAP[key]
                self.screen.addstr(20, 20, "Play Sound: {}".format(sound), curses.color_pair(3))
                subprocess.Popen(['mpg123', '-q', sound])

                self.screen.clrtoeol()
                self.screen.refresh()



if __name__ == '__main__':
    psb = PySoundBox()