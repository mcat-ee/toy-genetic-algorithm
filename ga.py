import sys
from arguments import arguments

import file_manager

if __name__ == "__main__":
    config_obj = arguments(sys.argv)
    messages = file_manager.load_messages_from_file(config_obj['message_file'])
    print(messages)
