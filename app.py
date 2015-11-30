import falcon
from controller import Amigos, Proximidade

app = falcon.API()
app.add_route('/amigos', Amigos())
app.add_route('/amigos_proximos', Proximidade())
