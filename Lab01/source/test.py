from re import search
from search import *

input1 = '../input/level_1/input1.txt'
input2 = '../input/level_1/input2.txt'
input3 = '../input/level_1/input3.txt'
input4 = '../input/level_1/input4.txt'
input5 = '../input/level_1/input5.txt'
input6 = '../input/level_2/input1.txt'
input7 = '../input/level_2/input2.txt'
input8 = '../input/level_2/input3.txt'


search_without_bonus(input1, dfs)
search_without_bonus(input1, bfs)
search_without_bonus(input1, ucs)
search_without_bonus(input1, gbfs, manhattan_distance)
search_without_bonus(input1, gbfs, euclidean_distance)
search_without_bonus(input1, astar, manhattan_distance)
search_without_bonus(input1, astar, euclidean_distance)

search_without_bonus(input2, dfs)
search_without_bonus(input2, bfs)
search_without_bonus(input2, ucs)
search_without_bonus(input2, gbfs, manhattan_distance)
search_without_bonus(input2, gbfs, euclidean_distance)
search_without_bonus(input2, astar, manhattan_distance)
search_without_bonus(input2, astar, euclidean_distance)

search_without_bonus(input3, dfs)
search_without_bonus(input3, bfs)
search_without_bonus(input3, ucs)
search_without_bonus(input3, gbfs, manhattan_distance)
search_without_bonus(input3, gbfs, euclidean_distance)
search_without_bonus(input3, astar, manhattan_distance)
search_without_bonus(input3, astar, euclidean_distance)

search_without_bonus(input4, dfs)
search_without_bonus(input4, bfs)
search_without_bonus(input4, ucs)
search_without_bonus(input4, gbfs, manhattan_distance)
search_without_bonus(input4, gbfs, euclidean_distance)
search_without_bonus(input4, astar, manhattan_distance)
search_without_bonus(input4, astar, euclidean_distance)

search_without_bonus(input5, dfs)
search_without_bonus(input5, bfs)
search_without_bonus(input5, ucs)
search_without_bonus(input5, gbfs, manhattan_distance)
search_without_bonus(input5, gbfs, euclidean_distance)
search_without_bonus(input5, astar, manhattan_distance)
search_without_bonus(input5, astar, euclidean_distance)

search_with_bonus(input6, astar_bonus, manhattan_distance)
search_with_bonus(input7, astar_bonus, manhattan_distance)
search_with_bonus(input8, astar_bonus, manhattan_distance)
search_with_bonus(input6, astar_bonus, euclidean_distance)
search_with_bonus(input7, astar_bonus, euclidean_distance)
search_with_bonus(input8, astar_bonus, euclidean_distance)
