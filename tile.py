from browser import window, document
import javascript

Phaser = window.Phaser

class Game(object):
    def __init__(self):
        config = {
            'type': Phaser.WEBGL,
            'width': 640,
            'height': 480,
            'backgroundColor': '#bfcc00',
            'scene': {
                'preload': self.preload,
                'create': self.create,
                'update': self.update
            }
        }
        self.game = window.Phaser.Game.new(config)
        self.UP = 0
        self.DOWN = 0
        self.LEFT = 0
        self.RIGHT = 0

    def preload(self, *args):
        this = javascript.this()
        this.load.image('food', 'assets/food.png')
        this.load.image('body', 'assets/body.png')

    def create(self, *args):
        this = javascript.this()

        def food(scene, x, y):
            Phaser.GameObjects.Image.call(this, scene)
            this.setTexture('food')
            this.setPosition(x * 16, y * 16)
            this.setOrigin(0)
            this.total = 0
            scene.children.add(this)
        self.Food = Phaser.Class.new({
            'Extends': window.Phaser.GameObjects.Image.call(this, this.scene),
            'initialize': food()
        })
        self.Snake = Phaser.Class.new({

        })


GAME = Game()