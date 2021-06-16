from browser import window, document
import javascript

Phaser = window.Phaser

class Game(object):
    def __init__(self):
        self.game = window.Phaser.Game.new(
            {
                'type': Phaser.AUTO,
                'width': 800,
                'height': 600,
                'pixelArt': 'true',
                'backgroundColor': '#1a1a2d',
                'scene': {
                    'preload': self.preload,
                    'create': self.create
                }
            }
        )

    def preload(self, *args):
        this = javascript.this()
        # this.load.setBaseURL('http://labs.phaser.io')
        this.load.image('tiles', 'http://labs.phaser.io/assets/tilemaps/tiles/drawtiles-spaced.png')
        this.load.image('car', 'http://labs.phaser.io/assets/sprites/car90.png')
        this.load.tilemapCSV('map', 'http://labs.phaser.io/assets/tilemaps/csv/grid.csv')

    def create(self, *args):
        this = javascript.this()

        self.map = this.make.tilemap({
            'key': 'map', 
            'tileWidth': 32, 
            'tileHeight': 32 
        })
        self.tileset = map.addTilesetImage('tiles', null, 32, 32, 1, 2)
        self.layer = map.createLayer(0, tileset, 0, 0)
        self.player = this.add.image(32+16, 32+16, 'car')

        # Left
        def left(event):
            tile = self.layer.getTileAtWorldXY(self.player.x - 32, self.player.y, true)
            if tile.index == 2:
                pass
            else:
                self.player.x -= 32
                self.player.angle = 180
        this.input.keyboard.on('keydown-A', left)

        # Right
        def right(event):
            tile = self.layer.getTileAtWorldXY(self.player.x + 32, self.player.y, true)
            if tile.index == 2:
                pass
            else:
                self.player.x += 32
                self.player.angle = 0
        this.input.keyboard.on('keydown-D', right)

        # Up
        def up(event):
            tile = self.layer.getTileAtWorldXY(self.player.x, self.player.y - 32, true)
            if tile.index == 2:
                pass
            else:
                self.player.x -= 32
                self.player.angle = -90
        this.input.keyboard.on('keydown-W', up)

        # Down
        def down(event):
            tile = self.layer.getTileAtWorldXY(self.player.x, self.player.y + 32, true)
            if tile.index == 2:
                pass
            else:
                self.player.x += 32
                self.player.angle = 90

        # demo code
        this.add.image(400, 300, 'sky')
        particles = this.add.particles('red')
        emitter = particles.createEmitter({
            'speed': 100,
            'scale': {'start': 1, 'end': 0},
            'blendMode': 'NORMAL'
        })
        this.input.keyboard.on('keydown-S', down)


GAME = Game()