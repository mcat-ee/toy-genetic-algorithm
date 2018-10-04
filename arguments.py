import json


def arguments(argv):
    '''
        Expects arguments of the form:
            ga.py message_file_location fitness_function_name population_count generations [test help]
    '''
    config = {}

    if 'test' in argv:
        config['test'] = True
    else:
        config['test'] = False
    try:
        argv.remove('test')
    except ValueError:
        pass

    if 'help' in argv:
        config['help'] = True
    else:
        config['help'] = False
    try:
        argv.remove('help')
    except ValueError:
        pass

    not_enough_arguments_flag = len(argv)< 5
    if config['help'] or not_enough_arguments_flag:
        if not_enough_arguments_flag:
            print("Not enough arguments provided")
        print_help_text()
        exit(0)

    config['message_file'] = argv[1]
    print("Message file location: '" + config['message_file'] +"'" )

    config['strategy_name'] = argv[2]
    print("Strategy nominated: '" + config['strategy_name'] + "'")

    config['population_size'] = int(argv[3])
    print("Population size chosen: '" + str(config['population_size']) + "'")

    config['generation_count'] = int(argv[4])
    print("Generation iterations chosen: '" + str(config['generation_count']) + "'")

    return config

def print_help_text():
    print("Help text printed")
