import openai

# Configuration for OpenAI API
class OpenAIConfig:
    def __init__(self):
        self.base_url = "http://localhost:1234/v1"
        self.api_type = "open_ai"
        self.api_key = "not-needed"

# Function to read file content.
# This setup allows your script to dynamically
# read the system message from the system_message.txt file, making it easy to update 
# the system message without changing the script's code.
def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to initiate conversation with the local-model and establishes roles and where the instructions come from.
def initiate_conversation(input_text, system_message):
    response = openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": input_text}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def main():
    # Instantiate configuration
    config = OpenAIConfig()
    openai.api_base = config.base_url
    openai.api_key = config.api_key

    # Read system message from file
    system_message = read_file_content("system_message.txt")
    if system_message is None:
        return

    # Conversation loop
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'bye', 'end']:
            print("Exiting the conversation.")
            break

        model_response = initiate_conversation(user_input, system_message)
        print("Model Response: ", model_response)

if __name__ == "__main__":
    main()
