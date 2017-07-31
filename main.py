#!/usr/bin/env python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import curses
import os
import subprocess
import thread
from time import sleep

import numpy as np
from pydub import AudioSegment

PATH = os.path.dirname(os.path.realpath(__file__))

SCREEN = curses.initscr()

curses.noecho()
curses.cbreak()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
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
        ord('g'): os.path.join(PATH, 'sounds/losgandules.mp3'),
        ord('b'): os.path.join(PATH, 'sounds/Boo2.mp3'),
        ord('B'): os.path.join(PATH, 'sounds/Boo2.mp3'),
    }
    _COLOR_RED = 1
    _COLOR_GREEN = 2
    _COLOR_BLUE = 4

    screen = None

    key_exit = ord('q')

    def __init__(self):
        self.screen = SCREEN
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

    def draw_audio(self, audio_src):
        audio = AudioSegment.from_file(audio_src)
        data = np.fromstring(audio._data, np.int16)

        BAR_HEIGHT = 120

        length = len(data)
        RATIO = float(length) / float(audio.duration_seconds * 100)
        count = 0
        maximum_item = 0
        max_array = []
        highest_line = 0

        for d in data:
            if count < RATIO:
                count = count + 1

                if abs(d) > maximum_item:
                    maximum_item = abs(d)
            else:
                max_array.append(maximum_item)

                if maximum_item > highest_line:
                    highest_line = maximum_item

                maximum_item = 0
                count = 1

        line_ratio = highest_line / BAR_HEIGHT

        for item in max_array:
            item_height = item / line_ratio if item != 0 else 0

            self.screen.addstr(30, 20, "".join(["#" for _ in range(item_height)]), curses.color_pair(4))
            self.screen.clrtoeol()
            self.screen.refresh()
            sleep(0.00955)

    def play_audio(self, sound):
        sleep(0.25)
        subprocess.Popen(['mpg123', '-q', sound])

    def loop(self):
        key = ''
        sound = self.SOUNDS_MAP[ord('o')]

        while key != ord('q'):
            key = self.screen.getch()
            if key in self.SOUNDS_MAP.keys():
                sound = self.SOUNDS_MAP[key]
                self.screen.addstr(20, 20, "Play Sound: {}".format(sound), curses.color_pair(3))
                thread.start_new_thread(self.play_audio, (sound,))
                thread.start_new_thread(self.draw_audio, (sound,))
                # self.draw_audio(sound)
                self.screen.clrtoeol()
                self.screen.refresh()
                self.draw_window()


if __name__ == '__main__':
    psb = PySoundBox()
