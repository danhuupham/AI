from search import *

# input folder
input_folder = '../input/'

# loop all the files in the level_1 folder
for file in os.listdir(input_folder + 'level_1'):
    search_without_bonus(input_folder + 'level_1/' + file, dfs)
    search_without_bonus(input_folder + 'level_1/' + file, bfs)
    search_without_bonus(input_folder + 'level_1/' + file, ucs)
    search_without_bonus(input_folder + 'level_1/' +
                         file, gbfs, manhattan_distance)
    search_without_bonus(input_folder + 'level_1/' +
                         file, gbfs, euclidean_distance)
    search_without_bonus(input_folder + 'level_1/' +
                         file, astar, manhattan_distance)
    search_without_bonus(input_folder + 'level_1/' +
                         file, astar, euclidean_distance)

# loop all the files in the level_2 folder
for file in os.listdir(input_folder + 'level_2'):
    search_with_bonus(input_folder + 'level_2/' +
                      file, gbfs, manhattan_distance)
    search_with_bonus(input_folder + 'level_2/' +
                      file, gbfs, euclidean_distance)
    search_with_bonus(input_folder + 'level_2/' +
                      file, astar, manhattan_distance)
    search_with_bonus(input_folder + 'level_2/' +
                      file, astar, euclidean_distance)

# loop all the files in the advance folder
for file in os.listdir(input_folder + 'advance'):
    search_with_portals(input_folder + 'advance/' + file, dfs)
    search_with_portals(input_folder + 'advance/' + file, bfs)
    search_with_portals(input_folder + 'advance/' + file, ucs)
    search_with_portals(input_folder + 'advance/' +
                        file, gbfs, manhattan_distance)
    search_with_portals(input_folder + 'advance/' +
                        file, gbfs, euclidean_distance)
    search_with_portals(input_folder + 'advance/' +
                        file, astar, manhattan_distance)
    search_with_portals(input_folder + 'advance/' +
                        file, astar, euclidean_distance)
