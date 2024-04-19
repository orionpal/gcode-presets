from gcode import *

# using what I know about the panels, helper functions for making each panel

directions = {
"UP" : (1,0),
"DOWN": (-1,0),
"RIGHT": (0,-1),
"LEFT": (0,1)
}
# for direction:
# imagine we start at the lower right corner of a panel
# imagine we move along the edge clockwise
# the direction for the cuts are just indicating where along that path we're cutting
#  * ->right-> *
# ^up^ PANEL vdownv
#  * <-left<-  *


# What ratios are we thinking for the roundness and indent? should be the thickness right?
def inner_joint(start, dist, thickness, direction, b):
    """
    make inner part of a finger joint with dogbone vertexes
    goes in by thickness
    returns string of gcode for commands
    """
    gcode = ""
    dir_adjust = directions[direction]
    indent_length = thickness-b

    # indent
    step_1_destination = (
        start[0] + indent_length * dir_adjust[0],
        start[1] + indent_length * dir_adjust[1]
        )
    # dogbone
    step_2_destination = (
        step_1_destination[0] + b * dir_adjust[0],
        step_1_destination[1] + b * dir_adjust[1]
    )
    step_2_center = (
        step_1_destination[0] + (b/2) * dir_adjust[0],
        step_1_destination[1] + (b/2) * dir_adjust[1],
    )
    # line across
    step_3_destination = (
        step_2_destination[0] - dist * dir_adjust[1],
        step_2_destination[1] - dist * dir_adjust[0]
    )
    # dogbone
    step_4_destination = (
        step_3_destination[0] - b * dir_adjust[0],
        step_3_destination[1] - b * dir_adjust[1]
    )
    step_4_center = (
        step_3_destination[0] + (b/2) * dir_adjust[0],
        step_3_destination[1] + (b/2) * dir_adjust[1],
    )
    # indent
    step_5_destination = (
        step_4_destination[0] - indent_length * dir_adjust[0],
        step_4_destination[1] - indent_length * dir_adjust[1]
    )

    # 1. go in thickness-bitSize inches (so that dogbone can be size of bit)
    gcode += line_gcode(step_1_destination) + "\n"
    return gcode
    # 2. stop and do a rotation for the dogbone
    gcode += curve_CCW_gcode(
        step_1_destination,
        step_2_destination,
        step_2_center) + "\n"
    # 3. go across the dist
    gcode += line_gcode(step_3_destination) + "\n"
    # 4. stop and do rotation for other dogbone
    gcode += curve_CCW_gcode(
        step_3_destination,
        step_4_destination,
        step_4_center) + "\n"
    # 5. go out some amount
    gcode += line_gcode(step_5_destination) + "\n"
    return gcode

def outer_joint(start, dist, thickness, direction, b):
    """
    make outer part of finger joint with dogbone vertexes
    goes out by thickness
    returns string of gcode for commands
    """
    gcode = ""
    dir_adjust = directions[direction]
    indent_length = thickness-b

    # dogbone
    step_1_destination = (
        start[0] - b * dir_adjust[0],
        start[1] - b * dir_adjust[1]
        )
    step_1_center = (
        start[0] - (b/2) * dir_adjust[0],
        start[1] - (b/2) * dir_adjust[1]
    )
    # indent
    step_2_destination = (
        step_1_destination[0] - indent_length * dir_adjust[0],
        step_1_destination[1] - indent_length * dir_adjust[1]
    )
    # line across
    step_3_destination = (
        step_2_destination[0] - dist * dir_adjust[1],
        step_2_destination[1] - dist * dir_adjust[0]
    )
    # indent
    step_4_destination = (
        step_3_destination[0] + indent_length * dir_adjust[0],
        step_3_destination[1] + indent_length * dir_adjust[1]
    )
    # dogbone
    step_5_destination = (
        step_4_destination[0] + b * dir_adjust[0],
        step_4_destination[1] + b * dir_adjust[1]
    )
    step_5_center = (
        step_4_destination[0] + (b/2) * dir_adjust[0],
        step_4_destination[1] + (b/2) * dir_adjust[1]
    )
    # 1. do a rotation for the dogbone
    gcode += curve_CCW_gcode(
        start,
        step_1_destination,
        step_1_center) + "\n"
    # 2. go out some amount
    gcode += line_gcode(step_2_destination) + "\n"
    # 3. go across the dist
    gcode += line_gcode(step_3_destination) + "\n"
    # 4. go in some amount
    gcode += line_gcode(step_4_destination) + "\n"
    # 5. stop and do rotation for other dogbone
    gcode += curve_CCW_gcode(
        step_4_destination,
        step_5_destination,
        step_5_center) + "\n"
    return gcode



# A
def all_innie_panel(start, edge, thickness, b):
    dist = edge/6
    gcode = ""

    # SOUTH
    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, dist,  thickness, "LEFT", b)
    start = (start[0]-dist, start[1])
    return gcode
    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # WEST
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, edge, thickness, "UP", b)
    start = (start[0], start[1]+dist)
    
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n\n"

    # NORTH

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, dist,  thickness, "RIGHT", b)
    start = (start[0]+dist, start[1])

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # EAST
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, edge, thickness, "DOWN", b)
    start = (start[0], start[1]-dist)
    
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n\n"

    return gcode
# B
def all_outie_panel(start, edge, thickness, b):
    dist = edge/6
    gcode = ""

    # SOUTH
    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, dist,  thickness, "LEFT", b)
    start = (start[0]-dist, start[1])

    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # WEST
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, edge, thickness, "UP", b)
    start = (start[0], start[1]+dist)
    
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n\n"

    # NORTH

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, dist,  thickness, "RIGHT", b)
    start = (start[0]+dist, start[1])

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # EAST
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, edge, thickness, "DOWN", b)
    start = (start[0], start[1]-dist)
    
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n\n"
    
    return gcode
# C
def half_half_panel(start, edge, thickness, b):
    dist = edge/6
    gcode = ""

    # SOUTH INNIE
    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, dist,  thickness, "LEFT", b)
    start = (start[0]-dist, start[1])

    start = (start[0]-dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # WEST OUTIE
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, edge, thickness, "UP", b)
    start = (start[0], start[1]+dist)
    
    start = (start[0], start[1]+dist)
    gcode += line_gcode(start) + "\n\n"

    # NORTH INNIE

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n"

    gcode += inner_joint(start, dist,  thickness, "RIGHT", b)
    start = (start[0]+dist, start[1])

    start = (start[0]+dist, start[1])
    gcode += line_gcode(start) + "\n\n"

    # EAST OUTIE
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n"

    gcode += outer_joint(start, edge, thickness, "DOWN", b)
    start = (start[0], start[1]-dist)
    
    start = (start[0], start[1]-dist)
    gcode += line_gcode(start) + "\n\n"
    
    return gcode
