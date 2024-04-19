from gcode import *
from .box_logic_helpers import *

def make_a_box(origin, BUFFER, e, t, b):
    gcode = ""
    # move to 0,0? idk some origin
    gcode += move_to_gcode(origin)
    # turn on spindle?
    gcode += f"M3 P100\n" # idk if this is right
    # PANELS
    # C A C
    # B B A
    #
    # 4 5 6
    # 3 2 1

    coordinate = origin

    # CREATE ALL PANELS

    # Create 1/A
    gcode += all_innie_panel(coordinate, e, t, b)
    return gcode
    # move over (do we need to turn off drill?)
    coordinate = (coordinate[0] - (e + BUFFER), coordinate[1])
    gcode += move_to_gcode(coordinate)

    # Create 2/B
    gcode += all_outie_panel(coordinate, e, t, b)

    # move over
    coordinate = (coordinate[0] - (e + BUFFER), coordinate[1])
    gcode += move_to_gcode(coordinate)

    # Create 3/B
    gcode += all_outie_panel(coordinate, e, t)

    # move over
    coordinate = (coordinate[0], coordinate[1] + (e + BUFFER))
    gcode += move_to_gcode(coordinate)

    # Create 4/C

    gcode += half_half_panel(coordinate, e, t)

    # move over
    coordinate = (coordinate[0] + (e + BUFFER), coordinate[1])
    gcode += move_to_gcode(coordinate)

    # Create 5/A
    gcode += all_innie_panel(coordinate, e ,t)

    # move over
    coordinate = (coordinate[0] + (e + BUFFER), coordinate[1])
    gcode += move_to_gcode(coordinate)

    # Create 6/C
    gcode += half_half_panel(coordinate, e, t)
    
    return gcode
