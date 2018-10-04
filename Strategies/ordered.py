from strategy import Strategy
from random import shuffle

name = "ordered"
def objective_function(genome):
    score = 0
    for messageIndex, message in enumerate(genome['ordered_message_list']):
        #print(messageIndex,message['id'])
        if str(messageIndex) == message['id']:
            score = score + 1

    return score

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
