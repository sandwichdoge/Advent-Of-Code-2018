#!/usr/bin/python
import re

#Process input file
fd = open("day3.txt", "r")
lines = fd.read().splitlines()
fd.close()

#I'm making a list'
coords_list = []
for line in lines:
        p = re.compile(r"@ (\d+),(\d+): (\d+)x(\d+)")
        pcoords = p.findall(line)
        coords_list.append(pcoords[0])

fabric = [[0 for i in range(1024)] for j in range(1024)]


#Part1
overlap_count = 0
for coords in coords_list:
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
for coords in coords_list: #I'm checking it twice
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])
        
        order += 1
        oflag = 0

        for y in range(top, top + height):
                for x in range(left, left + width):
                        if (fabric[y][x] > 1): #I'm gonna find out who's naughty
                                oflag = 1
                                break
        if (oflag == 0): #or nice
                print(order)
                break