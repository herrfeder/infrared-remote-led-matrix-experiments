#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import evdev
import threading
from utils import set_color
from Zruntext import RunText

global command_list
command_list = []

flirc=evdev.InputDevice('/dev/input/by-id/usb-flirc.tv_flirc-if01-event-kbd')

def read_remote(flirc):
    global command_list
    for event in flirc.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            attrib = evdev.categorize(event)
            if attrib.keystate == 1:
                print(attrib.keycode)
                if attrib.keycode is "KEY_R":
                    command_list.append("KEY_R")
                if attrib.keycode is "KEY_Y":
                    command_list.append("KEY_Y")
                if attrib.keycode is "KEY_G":
                    command_list.append("KEY_G")
                if attrib.keycode is "KEY_O":
                    command_list.append("KEY_O")
                if attrib.keycode is "KEY_B":
                    command_list.append("KEY_B")
                if attrib.keycode is "KEY_V":
                    command_list.append("KEY_V")
                if attrib.keycode is "KEY_Q":
                    command_list.append("KEY_Q")





def draw_line(n, pos,hor=False):
    pass




class RunLine(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunLine, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        global command_list
        remotet = threading.Thread(target=read_remote, args=(flirc,))
        remotet.start()

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        pos = offscreen_canvas.width
        timestep = 0.1
        number_lines = 1
        color_list = set_color(number_lines)
        border=0
        rev = False
        hor = False
        lineag = False
        last_key = ""

        #rt=RunText("Linien",80)
        #rt.process()
        #import os; print(os.getuid())
        
        while True:
            if command_list:
                last_key=command_list.pop()
            if last_key is "KEY_Q":
                last_key = ""
                break
            elif last_key is "KEY_R":
                last_key = ""
                rev = not rev
            elif last_key is "KEY_V":
                last_key = ""
                lineag = not lineag
            elif last_key is "KEY_G":
                last_key = ""
                hor = not hor
            elif last_key is "KEY_Y":
                last_key = ""
                print(timestep)
                if timestep == 0.00001:
                    timestep = 0.1
                else:
                    timestep = timestep / 10
            elif last_key is "KEY_O":
                last_key = ""
                if number_lines == 10:
                    number_lines = 1
                else:
                    number_lines += 1
                color_list = set_color(number_lines)
            elif last_key is "KEY_B":
                last_key = ""
                if border == 10:
                    border = 0
                else:
                    border += 1


            offscreen_canvas.Clear()
            
            
            if hor:
                for x in range(1,number_lines+1):
                    lineColor = set_color()
                    if lineag:
                        x = x+x*-1
                        pos = pos+pos*-1
                    graphics.DrawLine(offscreen_canvas, pos+x, 31, pos+x, 0, color_list[x-1])
                if border != 0:
                    redColor = graphics.Color(255,0,0)
                    for x in range(0,border):
                        graphics.DrawLine(offscreen_canvas, 0+border, 31, 0+border, 0, redColor)
                        graphics.DrawLine(offscreen_canvas, 31-border, 31, 31-border, 0, redColor)


            elif not hor:
                for x in range(1,number_lines+1):
                    lineColor = set_color()
                    graphics.DrawLine(offscreen_canvas, 0, pos+x, 31, pos+x, color_list[x-1])
                if border != 0:
                    redColor = graphics.Color(255,0,0)
                    for x in range(0,border):
                        graphics.DrawLine(offscreen_canvas, 0, 0+border, 31, 0+border, redColor)
                        graphics.DrawLine(offscreen_canvas, 0, 31-border, 31, 31-border, redColor)


            if rev:
                pos += 1
            elif not rev:
                pos -= 1

            if (pos <= 0+border-1):
                pos = 0+border-1
                color_list = set_color(number_lines)
                rev = not rev
            if (pos >= offscreen_canvas.width-border-2):
                pos = offscreen_canvas.width-border-2
                color_list = set_color(number_lines)
                rev = not rev


            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            
            time.sleep(timestep)
    
        offscreen_canvas.Clear()
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        return
        #remotet.join()



# Main function
if __name__ == "__main__":
    run_line = RunLine()
    if (not run_line.process()):
        run_line.print_help()
