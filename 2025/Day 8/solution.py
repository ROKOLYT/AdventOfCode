import json
import math
from collections import Counter

with open('formatted_input.json', 'r') as file:
    data = json.load(file)

def findSolution(data: list[dict[str, int]]) -> int:
    distances = calculateDistances(data)
    
    distances.sort(key=lambda item: item['distance'])
    
    parents: dict[int, int] = {}
    
    last_connected = (-1, -1)
    
    for i in range(len(data)):
        parents[i] = i

    # For the first part of the problem, we would run the loop only 1000 times.
    for i in range(len(distances)):
        item = distances[i]
        point1 = int(item['point1'])
        point2 = int(item['point2'])
        
        root1 = findRoot(parents, point1)
        root2 = findRoot(parents, point2)
        
        if root1 != root2:
            last_connected = (point1, point2)
            parents[root2] = root1
            
    circuit_counts: Counter[int] = Counter()
    for i in range(len(data)):
        root = findRoot(parents, i)
        circuit_counts[root] += 1
        
    top_3 = circuit_counts.most_common(3)
    
    result = 1
    for _, size in top_3:
        result *= size
        
    last_connected_distance = data[last_connected[0]]['x'] * data[last_connected[1]]['x']
    
    # For the first part of the problem, we would return the result variable.
    return last_connected_distance

def findRoot(parents: dict[int, int], point: int) -> int:
    if parents[point] != point:
        parents[point] = findRoot(parents, parents[point])
    return parents[point]
            
def calculateDistances(data: list[dict[str, int]]) -> list[dict[str, int | float]]:
    distances: list[dict[str, int | float]] = []
    
    for i, point in enumerate(data):
        x = point['x']
        y = point['y']
        z = point['z']
        
        for j, point2 in enumerate(data[i+1:]):
            x2 = point2['x']
            y2 = point2['y']
            z2 = point2['z']
            
            distance = calculateDistance((x, y, z), (x2, y2, z2))
            
            distances.append({
                'point1': i,
                'point2': i + 1 + j, 
                'distance': distance
            })
            
    return distances

def calculateDistance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

result = findSolution(data)
print(result)