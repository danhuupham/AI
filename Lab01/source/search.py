from utilities import *
from heuristic import *
from dfs import *
from bfs import *
from ucs import *
from gbfs import *
from astar import *


def search_without_bonus(input_file, algorithm, heuristic=None):
    bonus_points, matrix, start, end = read_file(input_file)
    cost, route, visited = algorithm(
        matrix, start, end, heuristic)

    output_folder = '../output/level_1/' + \
        input_file.split('/')[3].split('.')[0] + '/' + \
        algorithm.__name__ + '/'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if heuristic is not None and heuristic.__name__ == 'manhattan_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_1.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_1.jpg'
    elif heuristic is not None and heuristic.__name__ == 'euclidean_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_2.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_2.jpg'
    else:
        output_txt = output_folder + algorithm.__name__ + '.txt'
        output_jpg = output_folder + algorithm.__name__ + '.jpg'

    f = open(output_txt, 'w')
    f.write(str(cost))
    f.close()

    visualize_maze(matrix, bonus_points, start, end,
                   route, visited).savefig(output_jpg)


def search_with_bonus(input_file, algorithm, heuristic):
    bonus_points, matrix, start, end = read_file(input_file)
    cost, route, visited = astar(
        matrix, start, end, heuristic, bonus_points)

    output_folder = '../output/level_2/' + \
        input_file.split('/')[3].split('.')[0] + '/' + \
        algorithm.__name__ + '/'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if heuristic.__name__ == 'manhattan_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_1.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_1.jpg'
    elif heuristic.__name__ == 'euclidean_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_2.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_2.jpg'
    else:
        output_txt = output_folder + algorithm.__name__ + '.txt'
        output_jpg = output_folder + algorithm.__name__ + '.jpg'

    f = open(output_txt, 'w')
    f.write(str(cost))
    f.close()

    visualize_maze(matrix, bonus_points, start, end,
                   route, visited).savefig(output_jpg)


def search_with_portals(input_file, algorithm, heuristic=None):
    bonus_points, matrix, start, end, portals = read_file_with_portals(
        input_file)
    cost, route, visited = algorithm(
        matrix, start, end, heuristic, bonus_points, portals)

    output_folder = '../output/advance/' + \
        input_file.split('/')[3].split('.')[0] + '/' + \
        algorithm.__name__ + '/'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if heuristic is not None and heuristic.__name__ == 'manhattan_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_1.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_1.jpg'
    elif heuristic is not None and heuristic.__name__ == 'euclidean_distance':
        output_txt = output_folder + algorithm.__name__ + '_heuristic_2.txt'
        output_jpg = output_folder + algorithm.__name__ + '_heuristic_2.jpg'
    else:
        output_txt = output_folder + algorithm.__name__ + '.txt'
        output_jpg = output_folder + algorithm.__name__ + '.jpg'

    f = open(output_txt, 'w')
    f.write(str(cost))
    f.close()

    visualize_maze(matrix, bonus_points, start, end,
                   route, visited, portals).savefig(output_jpg)
