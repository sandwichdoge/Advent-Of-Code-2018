#!/usr/bin/python
import sys

def list_cmp(list1, list2):
        ret = 0
        for i in range(len(list1)):
                if(list1[i] != list2[i]):
                        ret += 1
        return ret


fd = open('day2.txt')
content = fd.read()
fd.close()
lines = content.splitlines()

#WHAT DO: find lines where letters appear twice and thrice
total2 = 0
total3 = 0
for line in lines:
        T = [0] * 128
        flg2 = False
        flg3 = False

        for c in line:
                T[ord(c)] += 1
        
        for m in T:
                if (m == 3): 
                        if not flg3: total3 += 1
                        flg3 = True
                elif (m == 2): 
                        if not flg2: total2 += 1
                        flg2 = True

print("Part1:", total2 * total3)


#PART 2
#Find lines with most common letters
for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
                diff = list_cmp(list(lines[i]), list(lines[j]))
                if (diff == 1):
                        sys.stdout.write("Part2: ")
                        for n in range(len(lines[i])):
                                if lines[i][n] == lines[j][n]: sys.stdout.write(lines[i][n])