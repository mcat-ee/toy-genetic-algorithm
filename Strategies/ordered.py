from strategy import Strategy
from random import shuffle
import random
name = "ordered"
def objective_function(genome):
    score = 0
    #print(genome)
    try:
        for messageIndex, message in enumerate(genome['ordered_message_list']):
            if str(messageIndex) == message['id']:
                score = score + 1
    except TypeError:
        score = 0
        for messageIndex, message in enumerate(genome):
            if str(messageIndex) == message['id']:
                score = score + 1
    return score

def generate_from_best(best_solution, population_size):
    #print(best_solution)
    population = []     #Population is created with the original best solution as it's founding member
    population.append({"id": best_solution['solution_object']['id'], "ordered_message_list": best_solution['solution_object']['ordered_message_list'][:]})
    id = 1
    while(len(population) < population_size):
        new_solution = best_solution['solution_object']['ordered_message_list'][:]
        solution_length = range(len(new_solution))
        index1, index2 = random.sample(solution_length, 2)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
        population.append({"id": str(best_solution['solution_object']['id']) + "-"+str(id), "ordered_message_list": new_solution})
        id = id + 1
    return population


def generate(message_list, population_size):
    solutions = []
    for solutionIndex in range(population_size):
        newlist = message_list[:]
        shuffle(newlist)
        solutions.append({
            "id": solutionIndex,
            "ordered_message_list": newlist
        })
    return solutions
