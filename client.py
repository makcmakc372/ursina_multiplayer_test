from ursina import Ursina, Entity, window
from ursina_multiplayer import GameClient


server = GameClient()

app = Ursina()

host_cube = Entity(model='cube')
client_cube = Entity(model='cube', position=(1, 0, 0))

def input(key):
    if key == 'd':
        client_cube.x += .5
    elif key == 'a':
        client_cube.x -= .5
    elif key == "w":
        client_cube.y += .5
    elif key == 's':
        client_cube.y -= .5

def update():
    server.send_entity_data(f'{client_cube.x}, {client_cube.y}')

    def update_host(content):
        xy_raw = content.split(', ')
        x = float(xy_raw[0])
        y = float(xy_raw[1])

        host_cube.x=x
        host_cube.y=y

    server.get_entity_data(update_host)

window.borderless = False

app.run()
