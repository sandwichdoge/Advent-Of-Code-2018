#Distance between 2 points
def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

fd = open("day6.txt", "r")
lines = fd.read().splitlines()
fd.close()

locations = []
for line in lines:
        coords = line.split(", ")
        for i in range(len(coords)):
                coords[i] = int(coords[i])
        locations.append(coords)

#Limit area size
MIN_X = 9999; MIN_Y = 9999; MAX_X = 0; MAX_Y = 0
for loc in locations:
        if loc[0] < MIN_X:
                MIN_X = loc[0]
        if loc[1] < MIN_Y:
                MIN_Y = loc[1]
        if loc[0] > MAX_X:
                MAX_X = loc[0]
        if loc[1] > MAX_Y:
                MAX_Y = loc[1]

print(MIN_X, MIN_Y, MAX_X, MAX_Y)
L = MIN_X; T = MIN_Y; W = MAX_X; H = MAX_Y
total_locations = len(locations)
total_points = MAX_X * MAX_Y
#Each point on map - x,y coords with array of distance to each location
points = [[[0 for i in range(total_locations + 2)] for x in range(MAX_X)] for y in range(MAX_Y)]

for y in range(MAX_Y):
        for x in range(MAX_Y):
                MIN = 999
                for loc in range(total_locations):
                        points[y][x][loc] = distance(x, y, locations[loc][0], locations[loc][1])
                        #if distance from point to location is the smallest without equals then point belongs to that location
                        if points[y][x][loc] < MIN:
                                MIN = points[y][x][loc]
                                points[y][x][total_locations] = loc #point belongs to loc
                        elif points[y][x][loc] == MIN:
                                points[y][x][total_locations] = 0 #belongs to nobody
                        points[y][x][total_locations + 1] += points[y][x][loc] #total distance too all locations

#PART 1
#List of eligible locations with coverage count
coverage = [0] * total_locations
for y in range(MAX_Y):
        for x in range(MAX_Y):
                owner = points[y][x][total_locations] #owner of current point
                coverage[owner] += 1

                if (x == L or x == W-1 or y == T or y == H-1): #edge = disqualify
                        coverage[owner] = -99999

print(max(coverage))

#PART 2
count = 0
for y in range(MAX_Y):
        for x in range(MAX_Y):
                _sum = points[y][x][total_locations + 1] #sum distance of current point
                if _sum < 10000:
                        count +=  1
print(count)