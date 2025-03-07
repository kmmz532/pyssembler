MOV R3, 10


_start:
MOV RCX, 5
MOV R1, 0
MOV R2, 2

A1:
ADD R1, R2
LOOP A1

PRINT "Hello, World!!"