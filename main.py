MAZE_LEN = 10;
antX,antY = [1,1]
maze = []

for _ in range(MAZE_LEN):
    maze.append(list(map(int,input().split())))

while True:
    maze[antY][antX] = 9
    if maze[antY][antX + 1] == 0:
        antX = antX + 1
    elif maze[antY][antX + 1] == 1:
        if maze[antY+1][antX] == 0 :
            antY = antY + 1
        elif maze[antY+1][antX] == 1:
            break
        elif maze[antY+1][antX] == 2:
            maze[antY+1][antX] = 9
            break
    else:
        maze[antY][antX + 1] = 9
        break

for y in range(MAZE_LEN):
    for x in range(MAZE_LEN):
        print(maze[y][x], end=" ")
    print()