from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from minigame.screenfactory import ScreenFactory
import minigame.locgenerator as locgenerator
from kivy.app import App
import kivy.properties as props

GAME_PREFIX = "cellid"

class CellScreen(ScreenFactory):
    """A class for displaying the cell id game screen."""
    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()
        self.generate_cell()
        

    def generate_cell(self):
        """Adds the cell parts to the screen."""
        img_locs = locgenerator.generate_picture_layout(self.imgs)
        counter = 0
        for label in self.orders:
            self.add_widget(CellButton(counter, label, img_locs[label]["source"], img_locs[label]["loc"], img_locs[label]["size"]))
            counter += 1
        self.parent

class CellButton(ButtonBehavior, Image):
    """A button image for a cell part."""
    def __init__(self, order, label, source_path, loc, size, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.source = source_path
        self.pos_hint = loc
        self.background_normal = ''
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = size
        self.label = label
        self.order = order

    def on_press(self):
        """Checks if the cell part that was tapped is correct."""
        if self.is_current():
            print("Correct " + self.label + " " + str(App.get_running_app().cur_img))
            if App.get_running_app().cur_img == App.get_running_app().last_img:
                print("Done")
            else:
                App.get_running_app().cur_img += 1
        else:
            print("Incorrect " + self.label + " " + str(App.get_running_app().cur_img))

    def is_current(self):
        """Returns if the cell part matches the current cell part label."""
        return self.order == App.get_running_app().cur_img
