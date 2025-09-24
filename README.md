# autonomous-delivery-agent-that-navigates-a-2D-grid-city-to-deliver-packages-no-ai-tool-used
An autonomous delivery agent for a 2D grid city using BFS, Uniform-Cost, A*, and local search replanning. It handles static obstacles, terrain costs, and moving obstacles with dynamic replanning. Includes Python CLI, test maps, experiments, and demo showcasing performance across static and dynamic environments.
City Grid Delivery Agent
Small project: a delivery bot in a grid-like city. It finds a path from start to goal.
Grid cells may have:

free road

blocked road

terrain with extra cost

moving blocks (simulate traffic)

Algorithms
BFS → shortest path when all roads same cost

UCS → respects terrain cost differences

A* → uses heuristic, usually faster

Hill Climb → with random restarts, tries again if stuck

What it shows
How different searches behave in maps

Measures: total cost, nodes visited, run time

Compare results across small and big maps

Setup
bash
git clone https://github.com/your-username/autonomous-city-delivery-agent.git
cd autonomous-city-delivery-agent
pip install -r requirements.txt
How to Run
bash
python city_agent.py --algo bfs
python city_agent.py --algo ucs
python city_agent.py --algo astar
Output is cost, path, explored nodes, and time.

Example
text
Algorithm: UCS
Path: [(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3)]
Cost: 6
Explored: 21
Time: 0.003s
License
MIT
