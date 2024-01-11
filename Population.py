from Chromosome import Chromosome
import random

class Population:
    def __init__(self, size, initial_cities, is_initial):
        self.chromosomes:Chromosome = []
        if is_initial == True:
            for i in range(size):
                self.chromosomes.append(Chromosome(random.sample(initial_cities, len(initial_cities))))

    def caluclate_fitness(self):
        for c in self.chromosomes:
            c.count_fitness_score()
        
        fit_values = [c.fitness for c in self.chromosomes]
        self.min_fit = min(fit_values)
        self.avg_fit = sum(fit_values) / len(fit_values)
        self.max_fit = max(fit_values)

    def get_best_and_worst_chromosome(self):
        self.caluclate_fitness()
        sorted_chromosomes = sorted(self.chromosomes, key= lambda x:x.fitness)
        return sorted_chromosomes[0], sorted_chromosomes[-1]

    