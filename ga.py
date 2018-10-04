import sys
from arguments import arguments

import Strategies.ordered
import file_manager

import pprint

if __name__ == "__main__":
    config_obj = arguments(sys.argv)
    messages = file_manager.load_messages_from_file(config_obj['message_file'])
    strategies = file_manager.import_libraries()
    pp = pprint.PrettyPrinter(depth=6)

    test_solutions = strategies['ordered']['generate'](messages['message_list'],3)
    for solution in test_solutions:
        pp.pprint(solution)
        print("SCORE: " + str(strategies['ordered']['objective_function'](solution)))
        print()
