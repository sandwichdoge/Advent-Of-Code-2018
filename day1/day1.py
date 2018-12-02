#!/usr/bin/python3

fd = open("day1.txt")
sum = 0
iter = 0
htable = {}

while (1):
        line = fd.readline()

        if not (line):
                fd.seek(0, 0)
                if (iter == 0): #1st part
                        print("Part 1:", sum)
                iter += 1
                continue

        if (htable.get(str(sum)) == 1):
                break

        htable[str(sum)] = 1
        sum += int(line)

fd.close()
print("Part 2. Found 1st repeated freq:", sum ,"in:", iter, "iterations")
