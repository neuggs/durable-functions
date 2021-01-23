# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    hello_name = yield context.call_activity('Hello', "John")
    user_name = hello_name.replace('Hello', '')
    reservation = yield context.call_activity('Reservation', user_name)
    gym_time = yield context.call_activity('GymTime', user_name)
    gym_time_response = ' ' + gym_time
    john_response = hello_name + ' ' + reservation + gym_time_response

    hello_name = yield context.call_activity('Hello', "Tony")
    user_name = hello_name.replace('Hello', '')
    reservation = yield context.call_activity('Reservation', user_name)
    gym_time = yield context.call_activity('GymTime', user_name)
    gym_time_response = ' ' + gym_time
    tony_response = hello_name + ' ' + reservation + gym_time_response

    hello_name = yield context.call_activity('Hello', "Jimmy")
    user_name = hello_name.replace('Hello', '')
    reservation = yield context.call_activity('Reservation', user_name)
    gym_time = yield context.call_activity('GymTime', user_name)
    gym_time_response = ' ' + gym_time
    jimmy_response = hello_name + ' ' + reservation + gym_time_response   
    
    return [john_response, tony_response, jimmy_response]

main = df.Orchestrator.create(orchestrator_function)