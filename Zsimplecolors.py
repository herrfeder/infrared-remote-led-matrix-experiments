#!/usr/bin/env python
from samplebase import SampleBase


class SimpleColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleColors, self).__init__(*args, **kwargs)
        self.color = args[0]
        #self.shape = args[1]
        print(self.color)

    def run(self):
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        while True:
            if self.color is "red":
                self.offscreen_canvas.Fill(255,0,0)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "orange":
                self.offscreen_canvas.Fill(255,128,0)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "yellow":
                self.offscreen_canvas.Fill(255,255,0)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "green":
                self.offscreen_canvas.Fill(0,255,0)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "turkis":
                self.offscreen_canvas.Fill(0,128,128)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "blue":
                self.offscreen_canvas.Fill(0,0,255)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "lila":
                self.offscreen_canvas.Fill(128,0,128)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
            if self.color is "violet":
                self.offscreen_canvas.Fill(128,0,255)
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)

