from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

def Cardinal_flip(d):
    if d == 'n':
        return 's'
    if d == 's':
        return 'n'
    if d == 'e':
        return 'w'
    if d == 'w':
        return 'e'


    # while len(storage) <len(room_graph)-1:
    #     if pointer.current_room.id not in storage:
    #         storage[pointer.current_room.id] = [pointer.current_room.get_exits()]
    #         back = back_track[-1]
    #         storage[pointer.current_room.id].remove(back)
    #     while len(storage[pointer.current_room.id]) < 1:
    #         back = back_track.pop()
    #         pointer.travel(back)
    #         travel.append(back)
    #     else:
    #         back = storage[pointer.current_room.id].pop()
    #         travel.append(back)
    #         back_track.append(Cardinal_flip(back))
    #         pointer.travel(back)



def GraphTraversal():
    pointer = player
    rooms = {}
    rooms[pointer.current_room.id] = pointer.current_room.get_exits()
    traversal_path = []
    backtrack_path = []
    while len(rooms) < len(room_graph)-1:
        if player.current_room.id not in rooms:
            rooms[player.current_room.id] = player.current_room.get_exits()
            last_room = backtrack_path[-1]
            rooms[player.current_room.id].remove(last_room)
        while len(rooms[player.current_room.id]) < 1:
            backtrack = backtrack_path.pop()
            player.travel(backtrack)
            traversal_path.append(backtrack)
        else:
            last_exit = rooms[player.current_room.id].pop()
            traversal_path.append(last_exit)
            backtrack_path.append(Cardinal_flip(last_exit))
            player.travel(last_exit)
    return traversal_path

path = GraphTraversal()
print(path)


traversal_path = path
# print(f"TRAVERSED PATHING {traversal_path}")


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# Bug Catch
def bug_catcher():
    storage_v = {}
    for x in visited_rooms:
        storage_v[x.id] = x.id
    for y in room_graph:
        if y in storage_v:
            pass
        else:
            print(y)
print("--#| ROOM CATCHER |#--")
bug_catcher()

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
