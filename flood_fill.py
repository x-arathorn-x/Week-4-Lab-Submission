from typing import List

board = [
    
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

positions_to_check = [
    [-1,0], # left
    [0,1], # top
    [1,0], # right
    [0,-1], # bottom
]

# for viewing printed iterations if needed,

def represent_board(board):
    for row in board:
        print(row)      
    print('------------------------')
            
            
def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    #checking if index should be filled
    if input_board[x][y] == old:
        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
        represent_board(input_board)
            
        
    for position in positions_to_check:
        new_x = x + position[0]
        new_y = y + position[1]
        # check if out of bounds
        if new_x >= len(input_board) or new_x < 0:
            continue
            
        if new_y >= len(input_board[new_x]) or new_y < 0:
            continue
            
        # continue with the fill...
        
        if input_board[new_x][new_y] == old:
             input_board[new_x] = input_board[new_x][:new_y] + new + input_board[new_x][new_y+1:]
             #recursion case
             flood_fill(input_board, old, new, new_x, new_y)
        
        
        
    return input_board
    
        

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....