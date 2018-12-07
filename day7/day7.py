import re 
import string
import sys


#return true if all items in dependencies are completed
def no_dependencies(status, dependencies):
        if dependencies == None: return True
        for item in dependencies:
                if (status.get(item) == 0):
                        return False
        return True


#BFKEGNOVATIHXYZRMCJDLSUPWQ

fd = open("day7.txt")
lines = fd.read().splitlines()
fd.close()

#Step T must be finished before step P can begin.
p = re.compile(r"Step (\w) must be finished before step (\w) can begin")
htable = {}
status = {} #0=INCOMPLETE, 1=COMPLETE

for line in lines:
        steps = p.findall(line)[0]
        step = steps[1]
        depend_on = steps[0]
        
        if htable.get(step) == None:
                new_list = []
                htable[step] = new_list

        htable[step].append(depend_on)
        htable[step].sort()


for item in [c for c in list(string.ascii_uppercase)]:
        status[item] = 0

for i in range(26): #alphabet count
        for item in status: #item = A-Z
                dependencies = htable.get(item)
                if no_dependencies(status, dependencies) and status[item] == 0:
                        sys.stdout.write(item)
                        status[item] = 1
                        break
