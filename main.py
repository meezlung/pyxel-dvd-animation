import pyxel
from random import randint

class ScreenProperty:
    width: int = 600
    height: int = 400

class DVDProperty:
    x_position: int = 20
    y_position: int = 15
    width: int = 50
    height: int = 50
    x_velocity: int = 5
    y_velocity: int = 5

class DVD:
    def __init__(self):
        self.dvd_property = DVDProperty()
        self.screen_property = ScreenProperty() 

        dvd = self.dvd_property
        screen = self.screen_property

        dvd.x_position = randint(0, screen.width)
        dvd.y_position = randint(0, screen.height)

        pyxel.init(screen.width, screen.height)
        self.curr_window_size = (pyxel.width, pyxel.height)

        pyxel.load('assets/dvd.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        dvd = self.dvd_property
        screen = self.screen_property
        
        if self.curr_window_size != (pyxel.width, pyxel.height):
            screen.width = pyxel.width
            screen.height = pyxel.height

        dvd.x_position += dvd.x_velocity
        dvd.y_position += dvd.y_velocity

        if dvd.x_position <= 0 or dvd.x_position + dvd.width >= screen.width:
            dvd.x_velocity *= -1
        if dvd.y_position <= 0 or dvd.y_position + dvd.height - 20 >= screen.height:
            dvd.y_velocity *= -1

    def draw(self):
        dvd = self.dvd_property
        
        pyxel.cls(0) # clear screen
        # pyxel.rect(dvd.x_position, dvd.y_position, dvd.width, dvd.height, 10)
        pyxel.blt(dvd.x_position, dvd.y_position, 0, 0, 0, 37, 27)

DVD()