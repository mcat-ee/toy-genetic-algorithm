import json

def arguments(argv):
    not_enough_arguments_flag = len(argv)< 3
    if 'help' in argv or not_enough_arguments_flag:
        if not_enough_arguments_flag: #TODO: Remove 'help' and 'test' from argv length check
            print("Not enough arguments provided")
        print_help_text()
        exit(0)

    config = {}
    if 'test' in argv:
        config['test'] = True
    else:
        config['test'] = False

    config['message_file'] = argv[1]
    print("Message file location: '" + config['message_file'] +"'" )
    return config

def print_help_text():
    print("Help text printed")
