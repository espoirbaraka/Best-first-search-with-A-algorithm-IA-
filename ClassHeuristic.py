import math
from ClassCoordonne import ClassCoordonne
class ClassHeuristic(ClassCoordonne):
    def __init__(self):
        super().__init__()
        #self.coord = ClassCoordonne()
    def haversine(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        R = 6371 # Earth radius in kilometers
        distance = 2*R*math.asin(math.sqrt(a))
        return distance
    def heuristic(self, cityA, cityB):
        lat1, lon1 = self.coordinates[cityA]
        lat2, lon2 = self.coordinates[cityB]
        return self.haversine(lat1, lon1, lat2, lon2)
    