from typing import List
import cv2
import numpy as np

w = 255 # wall
e = 0 # empty
f = 100 # filled

board = [
    [e,e,w,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
    [e,e,w,w,w,w,w,w,w,w,w,w,e,e,e,e,e,e,e,e],
    [e,e,w,e,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,w,e,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,e,w,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,e,w,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,e,w,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,e,w,w,w,w,w,e,e,e,w,e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e,w,w,w,w,e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
]

positions_to_check = [
    [-1,0], # left
    [0,1], # top
    [1,0], # right
    [0,-1], # bottom
]   
            
def flood_fill(input_board: List[str], x: int, y: int) -> List[str]:
    
    for position in positions_to_check:
        new_x = x + position[0]
        new_y = y + position[1]

        # check if out of bounds
        if new_x >= len(input_board[0]) or new_x < 0:
            continue
        if new_y >= len(input_board) or new_y < 0:
            continue
            
        # checking if pixel is empty and can be filled
        if input_board[new_y][new_x] == e:
            input_board[new_y][new_x] = f 
            # recursion case
            flood_fill(input_board, new_x, new_y)

        # show the result
        input_board = np.array(input_board, dtype='uint8')
        board_to_show = cv2.resize(input_board, (500,500))
        cv2.imshow('Board', board_to_show)
        cv2.waitKey(50)
        
    return input_board
       
modified_board = flood_fill(input_board=board, x=10, y=10)

# cleanup
cv2.destroyAllWindows()
print('Done!')



