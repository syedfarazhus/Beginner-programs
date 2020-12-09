
from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    '''Return a new list containing three counts: the number of elevations 
    from row number map_row of elevation_map that are less than, equal to, 
    and greater than elevation level.
    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]
    '''
    less_than = 0
    equal_to = 0
    greater_than = 0
    spec_row = elevation_map[map_row]
    for i in spec_row:
        if i < level:
                less_than += 1
        elif i == level:
                equal_to += 1
        elif i > level:
                greater_than += 1
    return [less_than, equal_to, greater_than]


def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    '''Modify elevation_map so that the elevation of each cell 
    between cells start and stop, inclusive, changes by amount  delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    '''

    startx, starty = start[0], start[1]
    endx, endy = stop[0], stop[1]
    while 1:
        if startx == endx and starty == endy:
            if not elevation_map[startx][starty] + delta < 1:
                elevation_map[startx][starty] += delta
                starty = starty + 1
                break
        if startx == endx:
            if not elevation_map[startx][starty] + delta < 1:
                elevation_map[startx][starty] += delta
                starty = starty + 1
                continue

        elif (starty == endy):
            if not elevation_map[startx][starty] + delta < 1:
                elevation_map[startx][starty] += delta
                startx = startx + 1
                continue



def get_average_elevation(elevation_map: List[List[int]]) -> float:
    '''Return the average elevation across all cells in elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    '''
    i = 0
    lump_sum = 0
    while i < len(elevation_map):
        lump_sum += sum(elevation_map[i])
        i += 1
    x = lump_sum / (len(elevation_map)) ** 2
    return x
            


def find_peak(elevation_map: List[List[int]]) -> List[int]:
    '''Return the cell that is the highest point in the elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    '''

    flat_list = []
    current_peak = 0
    for sub_list in elevation_map:
        for i in sub_list:
            flat_list.append(i)
    for i in flat_list:
        if i > current_peak:
            current_peak = i
    for sub_list in elevation_map:
        if current_peak in sub_list:
            return [elevation_map.index(sub_list), sub_list.index(current_peak)]
    

def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    '''Return True if and only if cell exists in the elevation_map
    and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    '''
    row = cell[0]
    column = cell[1]
    bool = False
    found_sinks = []
    pointLeft = -1
    pointRight = -1
    pointUp = -1
    pointDown = -1
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map[i])):
            focus_point = elevation_map[i][j]
            if(j>0):
                pointLeft = elevation_map[i][j-1]
            else:
                pointLeft = focus_point-1
            if (j < len(elevation_map[i])-1):
                pointRight= elevation_map[i][j+1]
            else:
                poinRight = focus_point-1

            if (i > 0):
                pointUp = elevation_map[i-1][j]
            else:
                pointUp = focus_point-1

            if (i < len(elevation_map)-1/len(elevation_map[i])-1):
                pointDown = elevation_map[i-1][j]
            else:
                pointUp = focus_point-1

            if(pointLeft>=focus_point and
            pointRight>=focus_point and
            pointUp>=focus_point and
            pointDown>=focus_point):
                bool = True
                found_sinks.append([i,j])

    return bool


def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    '''Return the local sink of cell cell in elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    '''

    row = cell[0]
    column = cell[1]
    list = []
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map[i])):
            if [i, j] == [row - 1, column] or [i, j] == [row + 1, column] or [i, j] == [row, column + 1] or [i, j] == [row, column - 1]:

                if elevation_map[row][column] > elevation_map[i][j]:
                    list.append(elevation_map[i][j])
                else:
                    continue

            elif [i, j] == [row - 1, column - 1] or [i, j] == [row - 1, column + 1] or [i, j] == [row + 1, column - 1] or [i, j] == [row + 1, column + 1]:

                if elevation_map[row][column] > elevation_map[i][j]:
                    list.append(elevation_map[i][j])
                else:
                    continue
    if not list:
        return cell
    number = min(list)
    loc = [0, 0]
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map)):
            if elevation_map[i][j] is number:
                loc[0] = i
                loc[1] = j
                break

        if elevation_map[i][j] is number:
            break

    return loc



def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    '''Return True if and only if a hiker can move from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False
    '''

    startx = start[0]
    starty = start[1]
    destx = dest[0]
    desty = dest[1]
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map)):
            if elevation_map[startx][starty] == elevation_map[destx][desty] and startx == destx and starty == desty:
                print("end")
                return True
            if supplies < 0:
                print('suplly end')
                return False

            if startx == destx:
                print("compare row")
                supplies -= abs(elevation_map[startx][starty] - elevation_map[startx][starty - 1])
                if supplies < 0:
                    continue
                starty = starty - 1
                continue

            elif (starty == desty):
                print("conpare col")
                supplies -= abs(elevation_map[startx][starty] - elevation_map[startx][starty - 1])
                if supplies < 0:
                    continue
                startx = startx - 1
                continue

            else:
                print("path")
                if abs(elevation_map[startx][starty] - elevation_map[startx - 1][starty]) <= abs(elevation_map[startx][starty] - elevation_map[startx][starty - 1]):
                    print('upper')
                    supplies -= abs(elevation_map[startx][starty] - elevation_map[startx - 1][starty])
                    print(supplies)
                    if supplies < 0:
                        continue
                    startx = startx - 1
                    continue
                elif abs(elevation_map[startx][starty] - elevation_map[startx - 1][starty]) > abs(elevation_map[startx][starty] - elevation_map[startx][starty - 1]):
                    print('left')

                    supplies -= abs(elevation_map[startx][starty] - elevation_map[startx][starty - 1])
                    if supplies < 0:
                        continue
                    starty = starty - 1
                continue


    
  
