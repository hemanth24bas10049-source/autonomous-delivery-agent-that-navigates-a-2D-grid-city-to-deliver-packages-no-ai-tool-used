# autonomous-delivery-agent-that-navigates-a-2D-grid-city-to-deliver-packages-no-ai-tool-used
An autonomous delivery agent for a 2D grid city using BFS, Uniform-Cost, A*, and local search replanning. It handles static obstacles, terrain costs, and moving obstacles with dynamic replanning. Includes Python CLI, test maps, experiments, and demo showcasing performance across static and dynamic environments.



City Grid Delivery Agent  

This project is about a delivery agent moving in a city set up as a 2D grid. The agent goes from a start point to a goal while:  
- avoiding blocked cells,  
- handling different terrain costs,  
- and adapting if obstacles shift.  

 Algorithms  
- BFS → finds shortest path (ignores costs)  
- UCS → considers terrain cost  
- A* → heuristic + cost, usually faster  
- Hill Climb → with restarts if stuck  

Essentials  
- Grid maps (small and big)  
- Supports static + moving obstacles  
- Tracks path, cost, explored nodes, and time  
- CLI tool to run and compare algorithms  



Prerequisites  
- Python **3.8+**  
- pip  

Install deps (if file exists):  
```bash
pip install -r requirements.txt
```
or just:  
```bash
pip install requests
```

Installation  

```bash
git clone https://github.com/your-username/autonomous-city-delivery-agent.git
cd autonomous-city-delivery-agent
```

(Optional) create venv:  
```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```



## Usage  

Run BFS:  
```bash
python city_agent.py --algo bfs
```

Run UCS:  
```bash
python city_agent.py --algo ucs
```

Run A*:  
```bash
python city_agent.py --algo astar
```



Example  

```
Algorithm: UCS
Path: [(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3)]
Cost: 6
Explored: 21
Time: 0.003s
```


## Tested API Endpoints  
- GET `/api/` – check alive  
- POST `/api/generate-test-map` – make maps  
- GET `/api/maps` – list maps  
- GET `/api/maps/{id}` – fetch map  
- POST `/api/pathfinding` – run BFS/UCS/A*/Hill  
- POST `/api/generate-report` – PDF of results  
- POST `/api/cli-command` – call CLI actions  
- POST `/api/maps` – upload custom map  



Contributing  
- Fork repo  
- Make a branch  
- Commit + push  
- Open PR  

License  
MIT  



