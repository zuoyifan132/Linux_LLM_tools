# Linux LLM Tools System

## Overview
The Linux LLM Tools System is a command-line tool designed to interact with a Linux environment by processing user commands in natural language. It uses an AI-powered model (such as OpenAI's API) to classify and execute various system operations like file, directory, and web operations. The system can run continuously to process user requests or handle one-time programmatic operations based on user inputs.

## Features
- **Natural Language Command Processing**: Users can input commands in natural language to perform basic Linux operations.
- **Predefined Operations**: Operations include file operations, directory operations, and web operations.
- **Continuous System Mode**: Allows the system to run continuously, processing user inputs in real-time.
- **One-Time Program Mode**: Run a single operation and exit.
- **AI-Driven Classification**: Uses an AI model to classify user intents and map them to supported operations.

## File Structure
- `main.py`: Entry point of the application. Initializes the tool in either system mode or one-time program mode and processes user inputs.
- `operation_classifier.py`: Contains functions to classify user inputs using OpenAI's API and validate whether the input matches supported operations.
- `tools_system.py`: Defines the `ToolsSystem` class, which runs the tool, processes user inputs, and manages the system state.
- `utilities.py`: Contains helper functions such as `refresh_print()` to provide feedback to the user during the operation.

## Requirements
- Python 3.6 or above
- Required Python libraries:
  - `openai`
  - `argparse`
  - `json`

You can install the dependencies via pip:
```bash
pip install openai argparse json
