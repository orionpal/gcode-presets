from .box_logic import *

# ---- Static Values (for now) -----

BUFFER = 0.4 # space away from each piece
origin = (0,0) # x,y tracker for drill bit
b = 3/8 # drill bit size/beam size

def create_box_gcode(filename, edge, thickness):
        """
        Takes in a filename,
        and edge length (in inches),
        and a thickness for the material (in inches)
        """
        with open(filename + ".txt", 'w') as file:
            gcode = make_a_box(origin, BUFFER, edge, thickness, b)
            file.write(gcode)
            return gcode