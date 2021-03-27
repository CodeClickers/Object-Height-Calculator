from kivy.config import Config

Config.set('graphics', 'window_state', 'visible')
Config.set('graphics', 'fullscreen', False)

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'position', 'auto')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.base import EventLoop
import time
import threading


class OHCApp(MDApp):
    def build(self):
        self.running = False
        self.seconds = 0
        self.inhome = True
        EventLoop.window.bind(on_keyboard=self.backbutton)
        return Builder.load_file("ui.kv")

    def on_stop(self):
        self.running = False

    def startstop_counter(self, *args):
        self.current = "tutorialscreen"
        if self.running:
            self.root.ids.startstop.text = "Start"

            self.running = False


        else:
            self.root.ids.startstop.text = "Stop"
            self.running = True
            threading.Thread(target=self.updatelabels).start()

    def changescreen(self, *args):
        self.inhome = False

    def reset_counter(self, *args):
        global m
        global ft
        self.running = False
        self.seconds = 0
        ft = 0
        m = 0

        self.root.ids.secondslabel.text = "0 seconds"
        self.root.ids.feetlabel.text = "0 feet"
        self.root.ids.meterslabel.text = "0 meters"

        self.root.ids.startstop.text = "Start"

    def updatelabels(self, *args):
        global ft
        global m
        while self.running:
            self.seconds += 0.1
            self.seconds = round(self.seconds, 1)
            self.root.ids.secondslabel.text = str(self.seconds) + " seconds"

            ft = 16 * (self.seconds ** 2)
            m = ft / 3.281
            ft = round(ft, 1)
            m = round(m, 1)
            self.root.ids.meterslabel.text = str(m) + " meters"
            self.root.ids.feetlabel.text = str(ft) + " feet"

            time.sleep(0.1)

    def backbutton(self, window, key, *largs):
        if key == 27:
            if not self.inhome:
                self.root.ids.screen_manager.current = "mainscreen"
                self.inhome = True
                return True

            else:
                pass


OHCApp().run()
