# 2차원 배열 입력, 출력
maze = []

for _ in range(10):
    maze.append(list(map(int,input().split())))

for y in range(10):
    for x in range(10):
        print(maze[y][x], end=" ")
    print()
