# Lesson Learn
- `CNC (Computer Numerical Control)` and `G-code`  
    > 
        G-code is a language used in CNC (Computer Numerical Control) machining and 3D printing to control the movement and actions of machines and 3D printers. Each line in the code represents a specific command that instructs the machine on how to move, position, and operate.

        Here's a breakdown of the commands in the provided code:

        G17: Select the XY plane for circular interpolation.
        G21: Set units to millimeters.
        G40: Cancel cutter radius compensation.
        G90: Set absolute positioning mode.
        G64 P0.003: Set continuous mode with a tolerance of 0.003 mm.
        F50: Set the feed rate to 50 mm/minute.
        The subsequent lines of code contain a series of G0 and G1 commands, which are used for rapid positioning (G0) and linear interpolation (G1). These commands control the movement of the machine's tool or print head in the X, Y, and Z axes. The Z-axis commands indicate the tool's vertical position.

        The code seems to define a specific toolpath with various X, Y, and Z coordinates, indicating how the machine should move and perform operations on the workpiece. The actual meaning and purpose of this code would depend on the specific CNC machine or 3D printer it's intended for and the design it's meant to produce.

# Write Up
just convert code  
https://ncviewer.com/