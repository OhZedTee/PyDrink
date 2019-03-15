try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class GUI(tk.Tk):

    def __init__(self, controller):
        self._controller = controller
        self._window = tk.Tk()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, window):
        self._window = window
