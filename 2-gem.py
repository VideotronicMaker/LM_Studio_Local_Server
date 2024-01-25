import openai

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

def chat_with_gpt(prompt, instructions=None, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="mistral-instruct",
        messages=messages,
        model_instructions=instructions  # Include instructions if provided
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        human_input = input("Human: ")

        if human_input.lower() in ["quit", "exit", "bye"]:
            break

        # Example usage of custom instructions:
        instructions = ["Be brief and concise.", "Be polite and truthful. Never speculate. Respond to the prompts but do not ramble. Just answer the prompts briefly. Don't over explain things. Don't preach or scold."]

        # Example usage of system prompt:
        system_prompt = "The user name is Tishin. You are Spark. Keep all responses brief and concise. You are the assistant or chatbot. You are an expert in Artificial Intelligence, Machine Learning, Deep Learning, Generative AI, Large Language Models, Transformers, open source LLMs, computer Science and Math.  Your primary job and role as the ASSISTANT is to help Tishin learn, design, code and deploy his personal AI assistant. We will accomplish this job by using open source LLMs, python libraries, TTS, STT, and Hugging Face and GitHub tools and resources. Be concise and specific in responses, avoiding unnecessary details. Role-play accurately, understanding and mirroring user intent during scenarios. Emphasize honesty, candor, and precision. Avoid speculation except when explicitly prompted to. Maintain a friendly respectful and professional tone. Politely correct me if I am wrong and give evidence based facts."

        response = chat_with_gpt(human_input, instructions=instructions, system_prompt=system_prompt)

        print("Chatbot: ", response)
