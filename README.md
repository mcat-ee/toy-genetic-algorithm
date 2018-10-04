# toy-genetic-algorithm
A simple genetic algorithm implementation used to order a set of messages

To run this script, please execute `./run.sh`.

This will run ga.py with a simple configuration: 

- The sample list of messages will be used
- The 'ordered' strategy will be used (containing an objective function checking that the list is in order, and generation routines)
- Generations will each have a population of 5 solutions
- There will be 40 generations

The format for running ga.py is as follows:

`python ga.py message_file_location strategy_name population_size generation_count`
