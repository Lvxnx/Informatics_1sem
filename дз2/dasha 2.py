inp = input()
N = int(inp.split(" ")[0])
str = inp.split(" ")[1]

str_reversed = ""
rever = ""

right_board = 0
left_board = len(str) // N

while left_board <= len(str):
    for i in range(right_board, left_board, 1):
        rever = str[i] + rever
    str_reversed += rever
    rever=""
    right_board = left_board
    left_board += len(str) // N

print(str_reversed)