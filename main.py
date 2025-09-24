import time, argparse, heapq
from collections import deque

class GridCity:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows, self.cols = len(grid), len(grid[0])

    def in_bounds(self, pos):
        r,c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors(self, pos):
        r,c = pos
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in steps:
            nr, nc = r+dr, c+dc
            if self.in_bounds((nr,nc)) and self.grid[nr][nc] != 1:
                yield (nr,nc)

    def cost(self, pos):
        return self.grid[pos[0]][pos[1]]

def reconstruct(came, start, goal):
    if goal not in came: return []
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = came[cur]
    return path[::-1]

def bfs(city):
    q = deque([city.start])
    came = {city.start: None}
    while q:
        cur = q.popleft()
        if cur == city.goal: break
        for n in city.neighbors(cur):
            if n not in came:
                came[n] = cur
                q.append(n)
    return reconstruct(came, city.start, city.goal), len(came)

def ucs(city):
    q = [(0, city.start)]
    came, cost_so_far = {city.start: None},{city.start:0}
    while q:
        cost, cur = heapq.heappop(q)
        if cur == city.goal: break
        for n in city.neighbors(cur):
            new_cost = cost_so_far[cur] + city.cost(n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                heapq.heappush(q,(new_cost,n))
                came[n] = cur
    return reconstruct(came, city.start, city.goal), cost_so_far.get(city.goal,None), len(came)

def astar(city):
    h = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])
    q = [(0, city.start)]
    came, cost_so_far = {city.start:None}, {city.start:0}
    while q:
        _, cur = heapq.heappop(q)
        if cur == city.goal: break
        for n in city.neighbors(cur):
            new_cost = cost_so_far[cur] + city.cost(n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                heapq.heappush(q,(new_cost+h(n,city.goal),n))
                came[n] = cur
    return reconstruct(came, city.start, city.goal), cost_so_far.get(city.goal,None), len(came)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", choices=["bfs","ucs","astar"], default="bfs")
    args = parser.parse_args()

    grid = [
        [0,0,0,0],
        [0,1,1,0],
        [0,0,2,0],
        [0,0,0,0]
    ]
    city = GridCity(grid,(0,0),(3,3))

    st = time.time()
    if args.algo=="bfs":
        path, explored = bfs(city)
        cost = len(path)-1
    elif args.algo=="ucs":
        path, cost, explored = ucs(city)
    else:
        path, cost, explored = astar(city)
    et = time.time()

    print("Algorithm:", args.algo.upper())
    print("Path:", path)
    print("Cost:", cost)
    print("Explored:", explored)
    print("Time:", round(et-st,4),"s")
