# Check If It Is a Straight Line
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope_start = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    for i in range(1, len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        slope = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
        if slope != slope_start:
            return False
    return True
print(checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]]))
