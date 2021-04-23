#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import evdev
import threading
from utils import set_color
from Zruntext import RunText
from Arunline import RunLine


flirc=evdev.InputDevice('/dev/input/by-id/usb-flirc.tv_flirc-if01-event-kbd')


modi = {1:RunLine}


def main():
    iterator = 0
    for event in flirc.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            attrib = evdev.categorize(event)
            if attrib.keystate == 1:
                if attrib.keycode is "KEY_N":
                    pc = modi[1](flirc)
                    pc.process()

if __name__ == "__main__":
    main()
