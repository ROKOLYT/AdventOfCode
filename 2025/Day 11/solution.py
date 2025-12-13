import json
from typing import Dict, List

with open('formatted_input.json', 'r') as f:
    data = json.load(f)


def findSolution(data: List[Dict[str, List[str]]]) -> int:
    graph: Dict[str, List[str]] = {}
    for entry in data:
        for node, neighbors in entry.items():
            graph[node] = neighbors
            
    memo: Dict[str, int] = {}

    def count_paths_from(current_node: str) -> int:
        if current_node == 'out':
            return 1
        
        if current_node in memo:
            return memo[current_node]
        
        total_paths = 0
        neighbors = graph.get(current_node, []) 
        
        for neighbor in neighbors:
            total_paths += count_paths_from(neighbor)
        
        memo[current_node] = total_paths
        return total_paths

    return count_paths_from('you')

def findSolutionNew(data: List[Dict[str, List[str]]]) -> int:
    graph: Dict[str, List[str]] = {}
    for entry in data:
        for node, neighbors in entry.items():
            graph[node] = neighbors

    def count_paths(start_node: str, target_node: str) -> int:
        memo: Dict[str, int] = {}

        def dfs(current: str) -> int:
            if current == target_node:
                return 1
            if current in memo:
                return memo[current]
            
            total = 0
            neighbors = graph.get(current, [])
            
            for neighbor in neighbors:
                total += dfs(neighbor)
            
            memo[current] = total
            return total

        return dfs(start_node)

    # 3. Calculate paths for Sequence A: svr -> dac -> fft -> out
    # We multiply the segments: (svr->dac) * (dac->fft) * (fft->out)
    svr_to_dac = count_paths('svr', 'dac')
    dac_to_fft = count_paths('dac', 'fft')
    fft_to_out = count_paths('fft', 'out')
    
    total_dac_first = svr_to_dac * dac_to_fft * fft_to_out

    svr_to_fft = count_paths('svr', 'fft')
    fft_to_dac = count_paths('fft', 'dac')
    dac_to_out = count_paths('dac', 'out')

    total_fft_first = svr_to_fft * fft_to_dac * dac_to_out

    return total_dac_first + total_fft_first

if __name__ == '__main__':
    answer = findSolutionNew(data)
    print(answer)