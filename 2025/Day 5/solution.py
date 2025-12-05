import json
from typing import List

with open('formatted_data.json', 'r') as file:
    data = json.load(file)
    
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    
    merged: List[List[int]] = []
    curr_start = intervals[0][0]
    curr_end = intervals[0][1]
    
    for start, end in intervals:
        if start > curr_end:
            merged.append([curr_start, curr_end])
            curr_start = start
            curr_end = end
            
        else:
            curr_end = max(curr_end, end)
            
    merged.append([curr_start, curr_end])
    
    return merged

def findSolution(intervals: List[List[int]], ids: List[int]) -> int:
    res = 0
    
    for id in ids:
        if isValid(intervals, id):
            res += 1
    
    return res
        
        
def isValid(intervals: List[List[int]], id: int) -> bool:
    for start, end in intervals:
        if start <= id <= end:
            return True
    return False

def freshIdCount(intervals: List[List[int]]) -> int:
    res = 0
    
    for start, end in intervals:
        res += end - start + 1
        
    return res

if __name__ == '__main__':
    merged = merge_intervals(data['intervals'])
    answer = findSolution(merged, data['ids'])
    print(answer)
    
    count = freshIdCount(merged)
    print(count)
            
    