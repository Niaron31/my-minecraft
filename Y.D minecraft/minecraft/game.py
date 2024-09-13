from direct.showbase.ShowBase import ShowBase
from map import Mapmanager
from hero import Hero
from direct.gui.OnscreenText import OnscreenText
class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.camera.setPos(0,24,3)
        self.camLens.setFov(60)
        self.land = Mapmanager()
        x,y,z = self.land.loadland("minecraft/land.txt")
        self.hero = Hero((5, y//2,9+12),self.land)
        self.skybox()
        # with open("land.txt") as f:
        #     for line in f:s
        #         print(line)
    def skybox(self):  

        self.sky = loader.loadModel("skybox/skybox.egg")
        self.sky.setScale(500)
        self.sky.setBin("background", 1)
        self.sky.setLightOff()
        self.sky.reparentTo(render)

 

game = Game()
game.run()

