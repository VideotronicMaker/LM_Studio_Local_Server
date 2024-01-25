import openai

# Set the base URL and API key for the OpenAI client
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

# Create a chat completion
completion = openai.ChatCompletion.create(
    model="local-model",  # this field is currently unused
    messages=[
        {"role": "system", "content": "Provide detailed technical explanations."},
        {"role": "user", "content": "Introduce yourself."}
    ],
    temperature=0.7,
)

# Print the chatbot's response
print(completion.choices[0].message.content)