from room import Room
from player import Player
from world import World
from graph import Graph
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# EXITS = player.current_room.get_exits()
# CURRENT ROOM = player.current_room.id
# need to initialize a visited
# Probably should backtrack at some point? Keep track of previous steps?
# mark every room, EACH TIME we go there
visited = {}
visited_exits = []
steps = 0

# print('room graph: ', room_graph)
# find your exits
# you start at room zero, so you don't need to add it to your traversal path
visited[player.current_room.id] = player.current_room.get_exits()
# print('visited: ', visited)
# print('visited: ', visited[player.current_room.id])
# for exits in player.current_room.get_exits():
#     unvisited_exits.append(exits)
# print('visited exits: ', visited_exits)
# while there are rooms to be visited
while len(visited) < len(room_graph) - 1:
    # if player hasn't been there
    if player.current_room.id not in visited:
        # put it in visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # keep track of last visited
        backtrack = visited_exits[-1]
        # go to an exit
        visited[player.current_room.id].remove(backtrack)
        # print('traversal path: ', traversal_path)
        # print('visited exits: ', visited_exits)
        # print('room: ', player.current_room.id)

        # when they have to backtrack
        # while they can backtrack
    while len(visited[player.current_room.id]) == 0:
        # backtrack
        # update prev
        backtrack = visited_exits.pop()
        # count that move
        traversal_path.append(backtrack)
        player.travel(backtrack)
    # going forward
    # similar to backtracking, keep track of next room
    forward = visited[player.current_room.id].pop(-1)
    if forward == 'n':
        visited_exits.append('s')
    if forward == 's':
        visited_exits.append('n')
    if forward == 'e':
        visited_exits.append('w')
    if forward == 'w':
        visited_exits.append('e')
    traversal_path.append(forward)
    player.travel(forward)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
