"""
Source: https://www.youtube.com/watch?v=rcGQxs7STvk

river length = []
set = {}
chech each point from top to bottom, left to right:
if not in set and it is 1: 
	include this point to the set
	river length = 1
		
    # Create a pointer called "downstream" to trace rivers
	downstream = get_downstream(current location)  

	# Trace down the river
	while downstream != None:
		include the downstream to the set
		current river length += 1	

		downstream = get_downstream(current downstream)
	record the river length # When the pointer is null, the river is at the end
"""

def get_adj(pos, matrix):
    y, x = pos
    adj = []

    if x >= 1:
        adj.append((y, x-1))
    if x < len(matrix[0]) - 1:
        adj.append((y, x+1))
    if y >= 1:
        adj.append((y-1, x))
    if y < len(matrix) - 1:
        adj.append((y+1, x))
    return adj

def get_downstream(pos, matrix, marked: set):
    """Check whether the inputted position have a "downstream". If yes, return the position
    of the downstream. If no, return None.
    """
    adj = get_adj(pos, matrix)

    # If there is a downstream of the input position
    for a in adj:
        if matrix[a[0]][a[1]] == 1 and a not in marked:
            return a
    
    # If the input position is the end of a river
    return None
    
def river_length(matrix):
    marked = set()
    river_len = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row, col) not in marked and matrix[row][col] == 1:
                marked.add((row, col))
                cur_river_len = 1
                downstream = get_downstream((row, col), matrix, marked)

                while downstream != None:
                    marked.add(downstream)
                    cur_river_len += 1

                    downstream = get_downstream(downstream, matrix, marked)
                
                river_len.append(cur_river_len)
                
    return river_len

matrix = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

print(river_length(matrix))