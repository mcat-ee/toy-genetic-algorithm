import json

def load_messages_from_file(file_location):
    messages = None
    with open(file_location) as f:
        messages = json.load(f)
    return messages
