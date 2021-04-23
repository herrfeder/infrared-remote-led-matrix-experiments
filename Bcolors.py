import multiprocessing
import evdev
from pulsingcolors import PulsingColors
from Zsimplecolors import SimpleColors

flirc=evdev.InputDevice('/dev/input/by-id/usb-flirc.tv_flirc-if01-event-kbd')

def simple_colors(color):
    pc = SimpleColors(color)
    pc.process()


P=None

for event in flirc.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        attrib = evdev.categorize(event)
        if attrib.keystate == 1:
            print(attrib.keycode)
            if attrib.keycode is "KEY_R":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('red',))
                P.start()
            if attrib.keycode is "KEY_O":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('orange',))
                P.start()
            if attrib.keycode is "KEY_Y":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('yellow',))
                P.start()
            if attrib.keycode is "KEY_G":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('green',))
                P.start()
            if attrib.keycode is "KEY_T":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('turkis',))
                P.start()
            if attrib.keycode is "KEY_V":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('violet',))
                P.start()
            if attrib.keycode is "KEY_L":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('lila',))
                P.start()
            if attrib.keycode is "KEY_B":
                if P:
                    P.terminate()
                    P = None
                P = multiprocessing.Process(target = simple_colors, args=('blue',))
                P.start()
            if attrib.keycode is "KEY_X":
                if P:
                    P.terminate()
                    P = None






















