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

#Find max fabric size
fh = 1024
fw = 1024
for coords in coords_list:
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])
        if (left + width > fw): fw = left + width
        if (top + height > fh): fh= top + height

fabric = [[0 for i in range(fh)] for j in range(fw)]


#Part1
count = 0
for coords in coords_list:
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])

        for y in range(top, top + height):
                for x in range(left, left + width):
                        if (fabric[y][x] == 1):
                                count+= 1
                        fabric[y][x] += 1

print(count)


#Part 2
order = 0
for coords in coords_list: #I'm checking it twice
        left = int(coords[0])
        top = int(coords[1])
        width = int(coords[2])
        height = int(coords[3])
        
        order += 1
        conflict = 0

        for y in range(top, top + height):
                for x in range(left, left + width):
                        if (fabric[y][x] > 1): #I'm gonna find out who's naughty
                                conflict = 1
                                break
        if (conflict == 0): #or nice
                print(order)
                break