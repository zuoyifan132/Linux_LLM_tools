import openai
import json

from utilities import refresh_print

client = openai.OpenAI()


# operation tools pool
# TODO: add more operations later
operation_tools_pool = ["dir_operation", "file_operation", "web_operation"]


def get_operation_tools_pool_string():
    formatted_string = "\n".join(f"- {operation}" for operation in operation_tools_pool)
    return formatted_string


def user_prompt_correctness(input_text: str) -> bool:
    """
    Check if user input matches our operation tools pool
    :param input_text: user prompt
    :return: return True if user intent is included in our operation tools pool, otherwise return False
    """

    function_descriptions = [
        {
            "name": "user_prompt_correctness",
            "description": "Determine if the user prompt's intend is included in our operation tools pool",
            "parameters": {
                "type": "object",
                "properties": {
                    "intend_correctness": {
                        "type": "string",
                        "description": f"""If the user prompt's intent is included in the following operation tools pool, 
                        set parameter to True, otherwise False.
                        ## operation tools pools:
                        {get_operation_tools_pool_string()} 
                        """,
                        "enum": [True, False]
                    },
                },
            },
            "required": ["intend_correctness"],
        }
    ]

    refresh_print("Checking operation correctness", "Executing")

    # get the openai response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input_text}
        ],
        functions=function_descriptions,
        function_call="auto"
    )
    output = response.choices[0].message
    func_params = json.loads(output.function_call.arguments)
    print(func_params)
    refresh_print("Checking operation correctness", func_params["intend_correctness"])

    res = func_params["intend_correctness"]
    if res:
        return True
    elif not res:
        return False
    else:
        print(f"user_prompt_correctness got unexpected value {res}")
        return None


def operation_classifier(input_text: str) -> str:
    """
    Classify the operation base on the input text
    :param input_text: The text that need to be classified with
    :return: The operation type
    """
    function_descriptions = [
        {
            "name": "operation_classifier",
            "description": "Classify which operation to use base on the input text",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation_type": {
                        "type": "string",
                        "description": """The user input which contains user intended operation
                    'dir_operation': directory operation like create, remove a directory etc.
                    'file_operation': file operation like create, copy, and remove a file etc.
                    'web_operation': web operation like open a website, download a file etc.""",
                        "enum": operation_tools_pool
                    },
                },
            },
            "required": ["operation_type"],
        }
    ]

    refresh_print("Classifying operation", "Executing")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": input_text}
            ],
            functions=function_descriptions,
            function_call="auto"
        )
        output = response.choices[0].message
        func_params = json.loads(output.function_call.arguments)
        refresh_print("Classifying operation", func_params["operation_type"])

        return func_params["operation_type"]
    except Exception as e:
        print(f"Error in operation_classifier: {e}")
        return "unknown_operation"


def main():
    print(type(user_prompt_correctness("I want to move a file into a another dir")))


if __name__ == "__main__":
    main()


# try:
#     # Command as a list of arguments
#     command = [func_params["command"], func_params["option"], func_params["path"]]
#     subprocess.run(command, check=True)
# except subprocess.CalledProcessError as e:
#     print(f"An error occurred while creating the directory: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
