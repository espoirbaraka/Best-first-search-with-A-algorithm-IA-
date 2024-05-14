from ClassHeuristic import ClassHeuristic
from ClassCoordonne import ClassCoordonne
class ClassAStar(ClassHeuristic, ClassCoordonne):
    def __init__(self):
        super().__init__()
        self.coo = ClassCoordonne()
        self.heurs = ClassHeuristic()
    
    def aStarSearch(self, graph, start, end):
        # Initialize the open set with the start city and its cost
        open_set = {start: 0}
        # Initialize the dictionary to store the parent of each city in the final path
        came_from = {}
        # Initialize the g_score dictionary with the cost from start to each city, defaulting to infinity
        g_score = {city: float('inf') for city in graph}
        g_score[start] = 0

        # While there are cities in the open set
        while open_set:
            # Select the city with the lowest cost from the open set
            current = min(open_set, key=open_set.get)

            # If the current city is the end city, reconstruct the path and return it
            if current == end:
                path = []
                while current != start:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, g_score[end]

            # Remove the current city from the open set and add it to the closed set
            del open_set[current]
            for neighbor, cost in graph[current].items():
                # Calculate the tentative g_score for the neighbor
                tentative_g_score = g_score[current] + cost
                # If the tentative g_score is lower than the current g_score for the neighbor, update the g_score and add the neighbor to the open set
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    open_set[neighbor] = tentative_g_score + self.heuristic(neighbor, end)

        # If no path is found, return None and infinity
        return None, float('inf')