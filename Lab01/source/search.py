from utilities import *
from heuristic import *
from dfs import dfs
from bfs import bfs
from ucs import ucs
from gbfs import gbfs
from astar import astar


def search_without_bonus(input_file, algorithm, heuristic=None):
    bonus_points, matrix, start, end = read_file(input_file)
    cost, route, visited = algorithm(
        matrix, start, end, heuristic)

    output_folder = '../output/' + input_file.split('/')[2] + '/' + \
        input_file.split('/')[3].split('.')[0] + '/' + \
        algorithm.__name__ + '/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if heuristic is not None and heuristic.__name__ == 'manhattan_distance':
        output_txt = output_folder + 'heuristic_' + algorithm.__name__ + '_1.txt'
        output_jpg = output_folder + 'heuristic_' + algorithm.__name__ + '_1.jpg'
    elif heuristic is not None and heuristic.__name__ == 'euclidean_distance':
        output_txt = output_folder + 'heuristic_' + algorithm.__name__ + '_2.txt'
        output_jpg = output_folder + 'heuristic_' + algorithm.__name__ + '_2.jpg'
    else:
        output_txt = output_folder + algorithm.__name__ + '.txt'
        output_jpg = output_folder + algorithm.__name__ + '.jpg'

    f = open(output_txt, 'w')
    f.write(str(cost))
    f.close()

    visualize_maze(matrix, bonus_points, start, end,
                   route, visited).savefig(output_jpg)


# def search_with_bonus(input_file, algorithm, heuristic=None):
#     bonus_points, matrix, start, end = read_file(input_file)

#     cost, route, visited = algorithm(
#         matrix, start, end, heuristic, bonus_points)

#     output = '../output/' + input_file.split('/')[2] + '/' + \
#         input_file.split('/')[3].split('.')[0] + '/' + \
#         algorithm.__name__ + '/'
#     if not os.path.exists(output):
#         os.makedirs(output)

#     f = open(output+algorithm.__name__ + '.txt', 'w')
#     f.write(str(cost))
#     f.close()

#     visualize_maze(matrix, bonus_points, start, end,
#                    route, visited).savefig(output+algorithm.__name__ + '.jpg')
