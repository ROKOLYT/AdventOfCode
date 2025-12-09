import json

with open('formatted_input.json') as f:
    data = json.load(f)
    
def findSolution(data: list[tuple[int, int]]) -> int:
    area = 0
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            
            area = max((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1), area)
            
    return area

def findSolutionNew(data: list[tuple[int, int]]) -> int:
    max_area = 0
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            width = abs(data[i][0] - data[j][0]) + 1
            height = abs(data[i][1] - data[j][1]) + 1
            rect_area = width * height
            
            rect_x1, rect_x2 = sorted([data[i][0], data[j][0]])
            rect_y1, rect_y2 = sorted([data[i][1], data[j][1]])
            
            valid = True
            
            for k in range(len(data)):
                edge_p1 = data[k]
                edge_p2 = data[(k + 1) % len(data)]
                
                edge_x1, edge_x2 = sorted([edge_p1[0], edge_p2[0]])
                edge_y1, edge_y2 = sorted([edge_p1[1], edge_p2[1]])
                
                if edge_y2 > rect_y1 and edge_y1 < rect_y2 and edge_x2 > rect_x1 and edge_x1 < rect_x2:
                    valid = False
                    break
                
            if valid:
                max_area = max(max_area, rect_area)
    
    return max_area
    
if __name__ == "__main__":
    answer = findSolutionNew(data)
    print(answer)