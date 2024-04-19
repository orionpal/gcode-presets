# ----------- gcode -------------

# just functions that give me gcode formatted strings

def line_gcode(destination):
    """
    This command moves the drill bit from the current position to the destination
    """
    return f"G01 X{destination[0]} Y{destination[1]}"

def curve_CW_gcode(start, end, center):
    """
    This command moves the drill bit clockwise from the start to the end around some center point
    """
    x = end[0]
    y = end[1]
    i = center[0]-start[0]
    j = center[1]-start[1]
    return f"G02 X{x}Y{y} I{i}J{j}"
def curve_CCW_gcode(start, end, center):
    """
    This command moves the drill bit counter-clockwise from the start to the end around some center point
    """
    x = end[0]
    y = end[1]
    i = center[0]-start[0]
    j = center[1]-start[1]
    return f"G03 X{x}Y{y} I{i}J{j}"

def move_to_gcode(destination):
    """
    This command moves to some destination but without the drillbit moving (I think?)
    """
    return f"G0 X{destination[0]} Y{destination[1]}\n"

# ---------- integration ------------

# --------- naive approach of doing square by square for a box -----------

