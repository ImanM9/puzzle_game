#This is the only file you need to work on. You do NOT need to modify other files

# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs() 
# ie iterative deepening depth first search


# here you need to implement the Iterative Deepening Search Method
import heapq

def astar(puzzle):

    open_set = []

    g_score = {tuple(puzzle): 0}

    start_node = (h(puzzle), puzzle, [])
    heapq.heappush(open_set, start_node)

    while open_set:
        _, current_puzzle, path = heapq.heappop(open_set)

        if current_puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # Goal state check
            return path

        for neighbor, move in get_neighbors(current_puzzle):
            tentative_g_score = g_score[tuple(current_puzzle)] + 1

            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                g_score[tuple(neighbor)] = tentative_g_score
                f_score = tentative_g_score + h(neighbor)
                heapq.heappush(open_set, (f_score, neighbor, path + [move]))

    return None

def h(puzzle):
    distance = 0
    for i, tile in enumerate(puzzle):
        if tile == 8:
            continue
        current_row, current_col = i // 3, i % 3
        goal_row, goal_col = tile // 3, tile % 3
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(puzzle):
    neighbors = []
    empty_index = puzzle.index(8)
    row, col = empty_index // 3, empty_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            swap_index = new_row * 3 + new_col
            new_puzzle = puzzle[:]
            new_puzzle[empty_index], new_puzzle[swap_index] = new_puzzle[swap_index], new_puzzle[empty_index]
            neighbors.append((new_puzzle, swap_index))

    return neighbors





def iterativeDeepening(puzzle):
    depth = 0
    while True:
        result = depthLimitedSearch(puzzle, depth)
        if result is not None:
            return result
        depth += 1

def depthLimitedSearch(puzzle, limit, path=[]):
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return path

    if limit <= 0:
        return None

    for neighbor in get_neighbors(puzzle):
        result = depthLimitedSearch(neighbor[0], limit - 1, path + [neighbor[1]])
        if result is not None:
            return result

    return None

def get_neighbors(puzzle):
    neighbors = []
    empty_index = puzzle.index(8)
    row, col = empty_index // 3, empty_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            swap_index = new_row * 3 + new_col
            new_puzzle = puzzle[:]
            new_puzzle[empty_index], new_puzzle[swap_index] = new_puzzle[swap_index], new_puzzle[empty_index]
            neighbors.append((new_puzzle, swap_index))

    return neighbors






