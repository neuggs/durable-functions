# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(name: str) -> str:
    if name == 'John':
        return 'and your gym time is 8:00 a.m. tomorrow.'
    elif name == 'Tony':
        return 'and your gym time is 3:00 p.m. on Friday.'
    else:
        return 'and your gym time is 6:30 a.m. Tuesday.'
