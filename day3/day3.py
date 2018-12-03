#!/usr/bin/python
import re

fd = open("day3.txt", "r")
lines = fd.read().splitlines()
fd.close()

#Initialize empty 2d array
fabric = [[0 for i in range(1024)] for j in range(1024)]

#Part1
overlap_count = 0
for line in lines:
        p = re.compile(r"@ (\d+),(\d+): (\d+)x(\d+)")
        pcoords = p.findall(line)
        coords = pcoords[0]
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])
        
        for y in range(top, top + height):
                for x in range(left, left + width):
                        if (fabric[y][x] == 1):
                                overlap_count+= 1
                        fabric[y][x] += 1

print(overlap_count)

#Part 2
order = 0
for line in lines:
        order += 1
        oflag = 0

        p = re.compile(r"@ (\d+),(\d+): (\d+)x(\d+)")
        pcoords = p.findall(line)
        coords = pcoords[0]
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])
        
        for y in range(top, top + height):
                for x in range(left, left + width):
                        if (fabric[y][x] > 1):
                                oflag = 1
                                break
        if (oflag == 0): 
                print(order)
                break