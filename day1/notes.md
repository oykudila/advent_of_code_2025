Puzzle input is a sequence of rotations, one per line.
L or R indicate the direction. 
The rotation has a distance value to indicate how many clicks to rotate in the direction.

e.g.
dial is at 11: 11 -> R8 -> 19
dial is at 19: 19 -> L19 -> 0
dial is at 0:   0 -> L1 -> 99
dial is at 99: 99 -> R1 -> 0


Dial starts at 50

The safe is a decoy, the actual password is the *number of times the dial points at 0 after any rotation in the sequence*

50 -> R60 -> 11

50 + 60 = 110 
110 


L50
50 -> L50 -> 0
L9
0 -> L9 -> 
L2
R42
R41
R5
R23
L26
R13
R3