import sys
from arguments import arguments
import Strategies.ordered
import file_manager

terminate_score = 10

def find_best_solution(solutions,objective_function):
    best_solution = {
        "solution_object": None,
        "score": -1
    }

    for solution in solutions:
        score = objective_function(solution)
        print(str(solution['id']) + " - SCORE: " + str(score))
        print("")
        if score > best_solution['score']:
            best_solution['solution_object'] = solution
            best_solution['score'] = score
    print("Best solution: " + str(best_solution['solution_object']['id']) + " with score: " + str(best_solution['score']))
    return best_solution

def run(strategy_name, population_size, generation_count):
    strategy = strategies[strategy_name]
    generate_function = strategy['generate']
    objective_function = strategy['objective_function']
    solutions = generate_function(messages['message_list'],population_size)

    for generation in range(generation_count):
        print("RUNNING GENERATION ", str(generation))
        best_solution = find_best_solution(solutions, objective_function)
        if best_solution['score'] == terminate_score:
            print("Found optimal solution in generation " + str(generation))
            break
        solutions = strategy['generate_from_best'](best_solution, population_size)


if __name__ == "__main__":
    config_obj = arguments(sys.argv)
    messages = file_manager.load_messages_from_file(config_obj['message_file'])
    strategies = file_manager.import_libraries()
    run('ordered', config_obj['population_size'], config_obj['generation_count'])
