# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import random

def main(name: str) -> str:
    randomnumber = random.randint(1, 32)

    if name == ' John!':
        return 'You are number ' + str(randomnumber) + ', your reservation is at 6:30 p.m.'
    elif name == ' Tony!':
        return 'You are number ' + str(randomnumber) + ', your reservation is at 7:20 p.m.'
    else:
        return 'You are number ' + str(randomnumber) + ', your reservation is at 9:00 p.m.'
    
