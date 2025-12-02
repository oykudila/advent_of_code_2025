Puzzle input is a sequence of rotations, one per line.
L or R indicate the direction. 
The rotation has a distance value to indicate how many clicks to rotate in the direction.

e.g.
dial is at 11: 11 -> R8 -> 19
dial is at 19: 19 -> L19 -> 0
dial is at 0:   0 -> L1 -> 99
dial is at 99: 99 -> R1 -> 0


For L:
1 -> L >=1 -> 0
2 -> L >=2 -> 0
3 -> L >=3 -> 0
.
.
.
97 -> L >=97 -> 0
98 -> L >=98 -> 0
99 -> L >=99 -> 0

For R:
1 -> R >=99 -> 0
2 -> R >=98 -> 0
3 -> R >=97 -> 0
.
.
.
97 -> R >=3 -> 0
98 -> R >=2 -> 0
99 -> R >=1 -> 0