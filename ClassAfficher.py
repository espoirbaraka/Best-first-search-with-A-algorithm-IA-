from ClassAStar import ClassAStar
from ClassCoordonne import ClassCoordonne
class ClassAfficher(ClassAStar, ClassCoordonne):
    def __init__(self):
        #super().__init__()
        ClassCoordonne.__init__(self)
        ClassAStar.__init__(self)
        self.astar = ClassAStar()
        self.graphe = ClassCoordonne()
        self.start_city = 'Goma'
        self.end_city = 'Kinshasa'
        self.path, self.cost = self.astar.aStarSearch(self.graphe.graph, self.start_city, self.end_city)

    def afficher(self):
        if self.path:
            print("Path from", self.start_city, "to", self.end_city, ":", self.path)
            print("Total cost:", self.cost)
        else:
            print("No path found from", self.start_city, "to", self.end_city)


a = ClassAfficher()
a.afficher()