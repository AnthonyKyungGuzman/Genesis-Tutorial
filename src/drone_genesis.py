import genesis as gs
import numpy as np

gs.init(backend=gs.gpu)

scene = gs.Scene(
    sim_options=gs.options.SimOptions(dt=0.01, gravity=(0, 0, -9.81)),
    show_viewer=True,
)

scene.add_entity(gs.morphs.Plane())

drone = scene.add_entity(
    morph=gs.morphs.Drone(
        file="urdf/drones/cf2x.urdf",
        model="CF2X",
        pos=(0.0, 0.0, 0.5),
    ),
)

scene.build()

for i in range(1000):
    scene.step()