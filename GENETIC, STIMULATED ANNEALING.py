#AI ASSIGNMENT 5                     
#QUES 1:
import random

items = {'A': {'weight': 45, 'value': 3},
         'B': {'weight': 40, 'value': 5},
         'C': {'weight': 50, 'value': 8},
         'D': {'weight': 90, 'value': 10}}

population_size = 4
max_capacity = 100
mutation_order = ['D', 'C', 'B', 'A']

initial_population = ['1111', '1000', '1010', '1001']

def calculate_fitness(individual):
    total_weight = sum(items[item]['weight'] for bit, item in zip(individual, items.keys()) if bit == '1')
    total_value = sum(items[item]['value'] for bit, item in zip(individual, items.keys()) if bit == '1')
    if total_weight <= max_capacity:
        return total_value
    else:
        return 0

def one_point_crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual):
    mutated_index = mutation_order.pop(0)
    mutation_order.append(mutated_index)
    index = list(items.keys()).index(mutated_index)
    individual = list(individual)
    individual[index] = '1' if individual[index] == '0' else '0'
    return ''.join(individual)

def select_fittest(population):
    sorted_population = sorted(population, key=calculate_fitness, reverse=True)
    return sorted_population[:2]

def genetic_algorithm(population):
    for _ in range(10):
        selected_individuals = select_fittest(population)
        if len(selected_individuals) >= 4:
            offspring1, offspring2 = one_point_crossover(selected_individuals[2], selected_individuals[3])
            offspring1 = mutate(offspring1)
            new_population = selected_individuals[:2] + [offspring1, offspring2]
            population = new_population
    return population

final_population = genetic_algorithm(initial_population)

print("Final Population after 10 iterations:")
for individual in final_population:
    print(individual, "Fitness:", calculate_fitness(individual))



#QUES 2:
import random

items = {'A': {'weight': 2, 'value': 3},
         'B': {'weight': 3, 'value': 5},
         'C': {'weight': 4, 'value': 7},
         'D': {'weight': 5, 'value': 9}}

population_size = 4
max_weight = 9
mutation_order = ['C', 'A', 'D', 'B']

initial_population = ['1111', '1000', '1010', '1001']

def calculate_fitness(individual):
    total_weight = sum(items[item]['weight'] for bit, item in zip(individual, items.keys()) if bit == '1')
    total_value = sum(items[item]['value'] for bit, item in zip(individual, items.keys()) if bit == '1')
    if total_weight <= max_weight:
        return total_value, total_weight
    else:
        return 0, 0

def one_point_crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual):
    mutated_index = mutation_order.pop(0)
    mutation_order.append(mutated_index)
    index = ord(mutated_index) - ord('A')
    individual = list(individual)
    individual[index] = '1' if individual[index] == '0' else '0'
    return ''.join(individual)

def select_fittest(population):
    sorted_population = sorted(population, key=lambda x: calculate_fitness(x)[0], reverse=True)
    return sorted_population[:2]

def genetic_algorithm(population):
    for _ in range(4):
        selected_individuals = select_fittest(population)
        if len(selected_individuals) >= 4:
            offspring1, offspring2 = one_point_crossover(selected_individuals[2], selected_individuals[3])
            offspring1 = mutate(offspring1)
            new_population = selected_individuals[:2] + [offspring1, offspring2]
            population = new_population
    return population

final_population = genetic_algorithm(initial_population)

print("Final Population after four iterations:")
for individual in final_population:
    fitness, weight = calculate_fitness(individual)
    print(individual, "Fitness:", fitness, "Weight:", weight)



#QUES 3:
import random
import math

def evaluate_solution(solution):
    """
    Evaluate the solution based on the number of satisfied clauses.
    """
    # Define the 2-SAT formula
    clause1 = (not solution[0] or solution[3])
    clause2 = (solution[2] or solution[1])
    clause3 = (not solution[2] or not solution[3])
    clause4 = (not solution[3] or not solution[1])

    # Count the number of satisfied clauses
    num_satisfied_clauses = sum([clause1, clause2, clause3, clause4])
    return num_satisfied_clauses

def movegen(solution):
    """
    Generate a new solution by randomly changing the value of one variable.
    """
    new_solution = list(solution)
    # Choose a random variable to flip
    var_to_flip = random.randint(0, 3)
    new_solution[var_to_flip] = not new_solution[var_to_flip]
    return new_solution

def simulated_annealing(initial_solution, T=500, cooling_function=lambda T: T - 50):
    current_solution = initial_solution
    current_value = evaluate_solution(current_solution)

    while T > 0:
        # Generate a new solution
        new_solution = movegen(current_solution)
        new_value = evaluate_solution(new_solution)

        # Calculate the energy difference
        delta_E = new_value - current_value

        # Accept the new solution if it's better or with a certain probability
        if delta_E > 0 or random.random() < math.exp(delta_E / T):
            current_solution = new_solution
            current_value = new_value

        # Update temperature
        T = cooling_function(T)

    return current_solution, current_value

if __name__ == "__main__":
    # Initial candidate solution
    initial_solution = [True, True, True, True]

    # Run simulated annealing
    final_solution, final_value = simulated_annealing(initial_solution, T=500)

    print("Final solution: {final_solution}")
    print("Number of satisfied clauses: {final_value}")



