# Import necessary libraries for the script.

import openai
# The openai library is employed for its core functionality to interact with llms, even though LM Studio operates without directly using the OpenAI API.
# LM Studio likely leverages a custom backend or local model deployment to bypass API calls, while still utilizing the openai library's interfaces for model interaction.

import os
# The os module in Python provides a way of using operating system dependent functionality like reading or writing to a file system, fetching environment variables, etc.

import logging
# The logging module is used to log messages for a library or application. This helps in debugging and understanding the flow of the program, especially during development and maintenance.

def read_file_content(file_path):
    """
    Reads and returns the content of a file specified by its path.

    This function attempts to open and read the content of the file located at 'file_path'.
    If the file is successfully opened, its content is returned as a string.
    In case the file is not found at the given path, the function logs an error message 
    indicating the file was not found and returns None.

    Parameters:
    file_path (str): The path to the file that needs to be read.

    Returns:
    str or None: The content of the file as a string if the file is found, otherwise None.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def chat_with_gpt(human_input, system_message):
    """
    Generates a response from the GPT model based on the user's input and a predefined system message.

    This function constructs a conversation structure for the GPT model, comprising a system message 
    and the user's input. It then sends this structure to the GPT model (specified as 'local-model') for processing.
    The function also sets a fixed temperature for the model's responses to control randomness.
    If the GPT model successfully generates a response, it is returned after being stripped of leading and trailing spaces.
    In case of any exceptions during the process, an error is logged, and a user-friendly error message is returned.

    Parameters:
    human_input (str): The user's input message to be sent to the GPT model.
    system_message (str): Predefined instructions or context for the GPT model.

    Returns:
    str: The GPT model's response or an error message in case of an exception.
    """
    try:
        messages = [{"role": "system", "content": system_message},
                    {"role": "user", "content": human_input}]
        
        temperature=0.7,

        response = openai.ChatCompletion.create(
            model="local-model",
            messages=messages
        )
        

        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "Sorry, an error occurred while processing your request."

def user_chatbot_conversation(system_message):
    """
    Initiates and manages a conversation loop with a chatbot.

    This function engages the user in a conversation with the chatbot. The conversation
    continues indefinitely until the user inputs a termination keyword ('quit', 'exit', or 'bye').
    Each user input is passed to the 'chat_with_gpt' function along with a predefined system message
    to generate a response from the chatbot, which is then printed.

    Parameters:
    system_message (str): A predefined system message used to provide context for the chatbot.

    The loop runs continuously, taking user input and printing the chatbot's response until the user
    decides to exit the conversation.
    """
    while True:
        human_input = input("Human: ").strip()

        if human_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(human_input, system_message)
        print("Chatbot: ", response)

if __name__ == "__main__":
    """
    Main execution block to initialize and run the chatbot conversation.

    This block sets up logging, loads necessary API configurations, and reads the system message
    from a text file. If the system message is successfully read, it initiates the chatbot conversation;
    otherwise, it informs the user about the missing system message file.
    """
    logging.basicConfig(level=logging.INFO)
    
    # Load API configuration
    openai.api_base = os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1")
    openai.api_key = os.getenv("OPENAI_API_KEY", "not-needed")

    # Read system message from file
    system_message = read_file_content("spark_custom_instructions.txt")

    if system_message:
        user_chatbot_conversation(system_message)
    else:
        print("System message not found. Please check the 'sparkle_custom_instructions.txt' file.")
