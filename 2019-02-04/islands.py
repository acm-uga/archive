def beachfront_cell(map, i, j):
    '''Returns the amount of beachfront for the cell at `map[i][j]`.

    The map is a grid of 1s and 0s where 1 means land and 0 means water.
    Beachfront is defined as any point where water borders land to the top,
    bottom, left, or right. Only land cells have beachfront (otherwise the
    same beachfront would be counted twice). Cells beyond the border of the map
    are always considered water.

    Arguments:
        map (2D rectangular list):
            The map of the island.
        i (int):
            The row coordinate of the cell.
        j (int):
            The column coordinate of the cell.

    Returns:
        beachfront (int):
            The amount of beachfront at `map[i][j]`.
    '''
    n_rows = len(map)
    n_cols = len(map[0])

    first_row = 0
    first_col = 0
    last_row = n_rows - 1
    last_col = n_cols - 1

    center = map[i][j]

    t = map[i - 1][j] if first_row < i else 0
    b = map[i + 1][j] if i < last_row else 0
    l = map[i][j - 1] if first_col < j else 0
    r = map[i][j + 1] if j < last_col else 0

    if center == 0:
        return 0
    else:
        beachfront = 0
        if t == 0: beachfront += 1
        if b == 0: beachfront += 1
        if l == 0: beachfront += 1
        if r == 0: beachfront += 1
        return beachfront


def beachfront_island(map):
    '''Returns the amount of beachfront for the island described by the map.

    The map is a grid of 1s and 0s where 1 means land and 0 means water.
    Beachfront is defined as any point where water borders land to the top,
    bottom, left, or right. Only land cells have beachfront (otherwise the
    same beachfront would be counted twice). Cells beyond the border of the map
    are always considered water.

    Arguments:
        map (2D rectangular list):
            The map of the island.

    Returns:
        beachfront (int):
            The amount of beachfront on the entire map.
    '''
    perimeter = 0
    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            perimeter += beachfront_cell(map, i, j)
    return perimeter


def test():
    assert beachfront_island([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]) == 16
