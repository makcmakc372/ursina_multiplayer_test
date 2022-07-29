from ursina import Ursina, Entity, window
from ursina_multiplayer import GameServer


server = GameServer()

app = Ursina()

host_cube = Entity(model='cube')
client_cube = None

def init_player(client):
    global client_cube

    client_cube = Entity(model='cube', position=(1, 0, 0))

server.on_client_connected(init_player)

def input(key):
    if key == 'd':
        host_cube.x += .5
    elif key == 'a':
        host_cube.x -= .5
    elif key == "w":
        host_cube.y += .5
    elif key == 's':
        host_cube.y -= .5
    elif key == 'escape':
        server.close_server()

def update():
    server.send_entity_data(f'{host_cube.x}, {host_cube.y}')

    def update_client(client, content):
        xy_raw = content.split(', ')
        x = float(xy_raw[0])
        y = float(xy_raw[1])

        client_cube.x=x
        client_cube.y=y

    server.get_client_entity_data(update_client)

window.borderless = False

app.run()
