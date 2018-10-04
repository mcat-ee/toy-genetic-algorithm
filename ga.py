import sys
from arguments import arguments

import Strategies.ordered
import file_manager

import pprint

def find_best_solution(solutions,objective_function):
    best_solution = {
        "solution_object": None,
        "score": -1
    }

    for solution in solutions:
        #pp.pprint(solution)
        score = objective_function(solution)

        print(str(solution['id']) + " - SCORE: " + str(score))
        print("")
        if score > best_solution['score']:
            best_solution['solution_object'] = solution
            best_solution['score'] = score
    print("Best solution: " + str(best_solution['solution_object']['id']) + " with score: " + str(best_solution['score']))


def run(strategy_name, population_size, generation_count):
        strategy = strategies[strategy_name]
        generate_function = strategy['generate']
        objective_function = strategy['objective_function']

        solutions = generate_function(messages['message_list'],population_size)

        find_best_solution(solutions, objective_function)

if __name__ == "__main__":
    config_obj = arguments(sys.argv)
    messages = file_manager.load_messages_from_file(config_obj['message_file'])
    strategies = file_manager.import_libraries()
    pp = pprint.PrettyPrinter(depth=6)

    run('ordered', config_obj['population_size'], config_obj['generation_count'])
