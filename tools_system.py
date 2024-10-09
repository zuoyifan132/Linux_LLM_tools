from enum import Enum
from operation_classifier import *


class Status(Enum):
    pending = "Pending"
    running = "Running"
    exit = "Exit"


class ToolsSystem:
    def __init__(self, mode):
        self.mode = mode
        self.status = Status.pending

    def run(self):
        self.status = Status.running

        # run forever
        if self.mode == "sys":
            while self.status != Status.exit:
                user_input = input("Please enter your request for the Linux OS: ")

                # check user exit
                if user_input == "exit":
                    self.status = Status.exit
                    print("Exiting Linux LLM tools system...")
                    continue

                # check user intent
                user_intent = user_prompt_correctness(user_input)
                # our operation tools pool doesn't include user prompt intent
                if not user_intent:
                    print("Our operation tools doesn't include your intent, please re-enter intent or exit")
                    continue

                operation = operation_classifier(user_input)
                print(operation)
