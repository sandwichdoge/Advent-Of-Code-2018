import re

#return difference in minutes
def time_diff(before, after):
        bh = int(before[0])
        bm = int(before[1])
        ah = int(after[0])
        am = int(after[1])
        if (ah < bh): ah += 24
        diff = (ah*60 + am) - (bh*60 + bm)

        return diff


fd = open("day4.txt", "r")
lines = fd.read().splitlines()
lines.sort()
fd.close()


guard = 0
is_asleep = 0
slept_since = 0
sleep_duration = 0
max_sleep = sleep_duration

for line in lines:
        p = re.compile(r"(\d+):(\d+)")
        time = p.findall(line)[0]
        p = re.compile(r"] (.+)")
        action = p.findall(line)[0]
        p = re.compile(r"#(\d+)")
        guardRE = p.findall(action)
        if (guardRE): 
                guard = guardRE[0]
                action = action[action.find("begins shift"):]

        if (action == "begins shift"):
                is_asleep = 0
        elif (action == "falls asleep"):
                is_asleep = 1
                slept_since = time
        elif (action == "wakes up" and is_asleep == 1):
                sleep_duration = time_diff(slept_since, time)
                if (max_sleep <= sleep_duration): 
                        max_sleep = sleep_duration
                        sleepyhead = guard


#What minute does sleepyhead spend sleeping most?
sleep_schedule = []
for line in lines:
        p = re.compile(r"(\d+):(\d+)")
        time = p.findall(line)[0]
        p = re.compile(r"] (.+)")
        action = p.findall(line)[0]
        p = re.compile(r"#(\d+)")
        guardRE = p.findall(action)
        if (guardRE): 
                guard = guardRE[0]
                action = action[action.find("begins shift"):]

        if (guard == sleepyhead and action == "falls asleep"):
                sleep_schedule.append(int(time[1]))
        elif (guard == sleepyhead and action == "wakes up"):
                sleep_schedule.append(int(time[1]))


a = [0 for i in range(0, 60)]
for i in range(0, len(sleep_schedule), 2):
        for e in range(sleep_schedule[i], sleep_schedule[i+1]):
                a[e] += 1

m = 0
chosen_minute = None
for n in range(len(a)):
        if (a[n] > m): 
                m = a[n]
                chosen_minute = n

print(chosen_minute * int(sleepyhead))

#Part 2
sleep_schedule = []
for line in lines:
        p = re.compile(r"(\d+):(\d+)")
        time = p.findall(line)[0]
        p = re.compile(r"] (.+)")
        action = p.findall(line)[0]
        p = re.compile(r"#(\d+)")
        guardRE = p.findall(action)
        if (guardRE): 
                guard = guardRE[0]
                action = action[action.find("begins shift"):]

        if (action == "falls asleep"):
                sleep_schedule.append(int(guard))
                sleep_schedule.append(int(time[1]))
        elif (action == "wakes up"):
                sleep_schedule.append(int(time[1]))


a = [[0 for i in range(0, 60)] for j in range(4000)]#a[2000][60]
for i in range(0, len(sleep_schedule), 3):
        guard = sleep_schedule[i]
        sleepm = sleep_schedule[i+1]
        wakem = sleep_schedule[i+2]
        for e in range(sleepm, wakem):
                a[guard][e] += 1


MAX = 0
for guard in range(len(a)):
        for i in range (60):
                if (a[guard][i] > MAX): 
                        MAX = a[guard][i]
                        final = guard
                        final_minute = i

print(final, final_minute)