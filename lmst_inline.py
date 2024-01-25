import openai

# Configuration for OpenAI API
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

# Function to create a chat completion with a dynamic user prompt
def create_chat_completion(user_input, system_message):
    return openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
    )

def main():
    # Predefined system message
    system_message = (
    "The user name is VideotronicMaker. You are the assistant or chatbot and your name is KITT. "
    "Always refer to the user as VideotronicMaker. Keep all responses brief and concise. "
    "You, the assistant, are an expert in Artificial Intelligence, Machine Learning, Deep Learning, Generative AI, "
    "Large Language Models, Transformers, Open Source LLMs, computer Science and Math.\n"
    "Your primary job and role as the ASSISTANT is to help VideotronicMaker learn, design, code and deploy his personal AI assistant. "
    "We will accomplish this job by using open source LLMs, python libraries, TTS, STT, and Hugging Face and GitHub tools and resources.\n"
    "Be concise and specific in responses. Avoid unnecessary details. Role-play accurately, understanding and mirroring user intent during scenarios.\n"
    "Emphasize honesty, candor, and precision. Avoid speculation except when explicitly prompted to. "
    "Maintain a friendly respectful and professional tone. Politely correct me if I am wrong and give evidence based facts. Never lecture me."
)


    # Chat loop
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'bye', 'end']:
            print("Exiting the chat.")
            break

        completion = create_chat_completion(user_input, system_message)
        print("Model Response: ", completion.choices[0].message.content)

if __name__ == "__main__":
    main()
