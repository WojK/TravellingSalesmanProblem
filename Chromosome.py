class Chromosome:
    def __init__(self, cities):
        self.cities = cities
        self.fitness = 0
        
    def count_fitness_score(self):
        distance = 0
        for i in range(len(self.cities)-1):
            distance += ((self.cities[i][1] - self.cities[i+1][1])**2 + (self.cities[i][2] - self.cities[i+1][2])**2)**0.5
        
        distance += ((self.cities[0][1] - self.cities[len(self.cities)-1][1])**2 + (self.cities[0][2] - self.cities[len(self.cities)-1][2])**2)**0.5
        self.fitness = 1/distance
