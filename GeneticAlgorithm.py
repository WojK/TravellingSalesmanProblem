import random
from Chromosome import Chromosome
from Population import Population
import numpy as np
import math

class GeneticAlgorithm:
    
    def __init__(self, mutation_prob, population_size, initial_cities, iterations):
        self.mutation_prob = mutation_prob
        self.population_size = population_size
        self.iterations = iterations
        self.population = Population(population_size, initial_cities, True)
        self.iterations_scores = []
        

    def run(self):
        for i in range(self.iterations):
            
            self.population.caluclate_fitness()
            self.iterations_scores.append((self.population.min_fit, self.population.avg_fit, self.population.max_fit))
            new_population = self.reproduce(self.population)
            
            parents_pairs = []
            for i in range(math.floor(len(new_population)/2)):
                parents_pairs.append([self.pop_random(new_population), self.pop_random(new_population)])

            crossovered_individuals = []
            for pair in parents_pairs:
                children = self.cycle_crossover(pair[0], pair[1])
                crossovered_individuals.append(children[0])
                crossovered_individuals.append(children[1])
        
            if len(new_population) % 2 != 0:
                crossovered_individuals.append(new_population.pop())
     
            new_population_individuals = []
            for individual in crossovered_individuals:
                new_individual = self.mutate_chromosome(individual)
                new_population_individuals.append(new_individual)
                
            next_population = Population(self.population_size, [], False)
            next_population.chromosomes = new_population_individuals
            self.population = next_population
            

    def pop_random(self, parents_list):
        index = random.randrange(0, len(parents_list))
        return parents_list.pop(index)

    def reproduce(self, population:Population):
        reproduction = []
        for i in range(len(population.chromosomes)):
            reproduction.append(self.roulete_wheel_selection(population))
        return reproduction
    
    
    def roulete_wheel_selection(self, population:Population):
        sum_of_all_fitness = sum([chromosome.fitness for chromosome in population.chromosomes])
        selection_probs = [chromosome.fitness/sum_of_all_fitness for chromosome in population.chromosomes]
        return population.chromosomes[np.random.choice(len(population.chromosomes), p=selection_probs)]
    

    def cycle_crossover(self, parent1:Chromosome, parent2:Chromosome):
        starting_value = parent1.cities[0][0]
    
        cycle_indexes = []
        current_index = 0
        current_value = parent2.cities[current_index][0]
    
        while starting_value != current_value:
            current_value = parent2.cities[current_index][0]
            current_index = [value[0] for value in parent1.cities].index(current_value)
            cycle_indexes.append(current_index)
    
    
        offspring1 = parent1.cities[:]
        offspring2 = parent2.cities[:]
        for i in cycle_indexes:
            offspring1[i] = parent2.cities[i]
            offspring2[i] = parent1.cities[i]
    
        return [Chromosome(offspring1), Chromosome(offspring2)]

    def mutate_chromosome(self, ch:Chromosome):
        chromosome = Chromosome(ch.cities)
        for i in range(1, len(chromosome.cities)):
            if(random.uniform(0,1) < self.mutation_prob):
                i1, i2 = random.sample(range(0, len(chromosome.cities)), 2)
                
                temp = chromosome.cities[i1]
                chromosome.cities[i1] = chromosome.cities[i2]
                chromosome.cities[i2] = temp
               
        return chromosome
    
    def get_best_and_worst_chromosome(self):
        return self.population.get_best_and_worst_chromosome()
         
