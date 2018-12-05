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


fd = open("big boye.txt", "r")
lines = fd.read().splitlines()
lines.sort()
fd.close()


#Parse and make sense of input
guard = 0
is_asleep = 0
slept_since = 0
sleep_duration = 0
max_sleep = sleep_duration

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


a = [[0 for i in range(0, 60)] for j in range(5000)]#a[4000][60]
total = [0] * 5000
for i in range(0, len(sleep_schedule), 3):
        guard = sleep_schedule[i]
        sleepm = sleep_schedule[i+1]
        wakem = sleep_schedule[i+2]
        for e in range(sleepm, wakem):
                a[guard][e] += 1
                total[guard] += 1


#Part 1
sleepyhead = int(total.index(max(total)))
chosen_minute = a[sleepyhead].index(max(a[sleepyhead]))

print(chosen_minute * sleepyhead)


#Part 2
MAX = 0
for guard in range(len(a)):
        for i in range (60):
                if (a[guard][i] > MAX): 
                        MAX = a[guard][i]
                        final = guard
                        final_minute = i

print(final * final_minute)