import json
from Strategies import ordered

def load_messages_from_file(file_location):
    messages = None
    with open(file_location) as f:
        messages = json.load(f)
    return messages

def import_libraries():
    strategies = {}
    strategies[ordered.name] = { "objective_function": ordered.objective_function, "generate": ordered.generate}
    return strategies
