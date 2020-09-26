# The Wrong idea here, we are not contrlling the character directly
# We are creating a parth for him to go through.

# ---------------------------------------------------- Debug Code
# print(f"Visited ROOMS --|>{visited_rooms}\n")
# for x in visited_rooms:
#     print(x)

print("---| Start |---\n __Code Controls__\n")
print(player.current_room.get_exits())
    # This will get the room's possible exits.
print("This will travel north now and get:")
    #  This will move our pointer/player around.
player.travel("n")
print(player.current_room.get_exits())

    #This is how to add the new found room. 
visited_rooms.add(player.current_room)
print("---| End |---\n")


# ---------------------------------------------------- Debug Code

#  --------------ATT 1:
def GraphTraversal(start, world):
    path = []
    revPath = []
    visited = set()
    fork = deque()
    queue = deque()
    queue.append([start])
    def Outgoing():
        newPath = list(currPath)
        newPath.append(destinations[room])
        path.append(room)
        revPath.append(Cardinal_flip(room))
        queue.append(newPath)

 
    while len(queue) >0:
        currPath = queue.popleft()
        currQue = currPath[-1]
        location = world[currQue][0]
        destinations = world[currQue][1]
        visited.add(location)
        print(f" ==>==>{currQue}")
        for room in destinations:
            print(f"curr room:  {room}")
            if world[destinations[room]][0] not in visited:
                Outgoing()
            else:
                revPath.reverse()
                path = path + revPath
                revPath.clear()
    print(f"Path {path}")
    print(f"RebPath {revPath}")
    print(f"Visited Rooms: {visited}")
    return path
    #  --------------ATT 1:

    #  --------------ATT 2:
    #  FARRR TO MANY MOVES
    def rec_path_sort(hold, path):
    if len(path) == 1:
        location = path.pop()
        hold[location] = "end"
    else:
        location = path.pop(0)
        hold[location] = rec_path_sort(hold, path)

def GraphTraversal(start, world):
    end = {}
    hold = {}
    queue = deque()
    queue.append([('',start)])
    visited = set()
    while len(queue) > 0:
        currPath = queue.popleft()
        currLoc = currPath[-1][1]
        rooms = world[currLoc]
        visited.add(rooms[0])
        for entrance in rooms[1]:
            if world[rooms[1][entrance]][0] not in visited:
                newPath = list(currPath)
                newPath.append((entrance,rooms[1][entrance]))
                queue.append(newPath)
            else:
                newPath = list(currPath)
                endPaths = list(currPath)
                rec_path_sort(end,endPaths)
                currNode = newPath[0]
                if currNode[1] in hold:
                    hold[newPath[0][1]].append(newPath)
                else:
                    hold[newPath[0][1]]= []
                    hold[newPath[0][1]].append(newPath)
    filtered = set()
    path = {}
    cardinal_path = []
    for location in end:
        if end[location] == 'end':
            filtered.add(location)
    print(filtered)
    for x in hold[0]:
        if x[-1] in filtered:
            x.pop(0)
            print(f"x in hold {x}")
            if x[-1] not in path:
                path[x[-1]] = x
    for x in path:
        print(f"x in path {path[x]}")
    for x in path:
        storage = []
        flipped = []
        for y in path[x]:
            storage.append(y[0])
            flipped.append(Cardinal_flip(y[0]))
        total = storage+flipped[::-1]
        cardinal_path = cardinal_path + total
    return cardinal_path

# ----------
    visited = set()
    queue = deque()
    pioneer = Player(world.starting_room)
    queue.append([pioneer.current_room.id])
    paths = []
    while len(queue) > 0:
        print(f"Queue{queue}")
        currPath = queue.popleft()
        currNode = currPath[-1]
        if currNode in visited:
            continue
        # if  currNode not in visited:
        #     print(f" currpath {currPath}")
        #     paths.append(currPath)
        if currNode not in visited:
            visited.add(currNode)
            for door in pioneer.current_room.get_exits():
                if currNode not in storage:
                    move = pioneer
                    move.travel(door)
                    storage[currNode] = [{door: move.current_room.id}]
                    storage[move.current_room.id] = [{Cardinal_flip(door): currNode}]
                    newPath = list(currPath)
                    newPath.append(move.current_room.id)
                    queue.append(newPath)
                else: 
                    move = pioneer
                    move.travel(door)
                    storage[currNode].append({door:move.current_room.id})
                    newPath = list(newPath)
                    newPath.append(move.current_room.id)
                    queue.append(newPath)     
    print(f"Path -- {paths}")