import openai
import os

# Derive API-key from an environment variable.
# How2: Set API-key for Windows: setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")


# Model Variables
model_name = "gpt-3.5-turbo"
system_prompt = "You are a voice assistant."

# Chat Variables
completion_tokens = 0
prompt_tokens = 0
total_tokens = 0

# Pricing
input_pricing = 0.016
output_pricing = 0.021
currency = "NOK"


messages = []
chat_count = 0
chat_max = 1


# Function to prompt the OpenAI model with a list of messages and return the generated response.
def prompt_model(messages):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    return (response.choices[0].message.content, response)


# Introduction
print(f"You are using {model_name}")


# Append system prompt to the messages list
messages.append({"role": "system", "content": system_prompt})


while True:
    # Get user input and add it to the messages list.
    user_prompt = input("> ")
    messages.append({"role": "user", "content": user_prompt})

    # Get assistant output
    api_output = prompt_model(messages)[1]
    print(api_output)
    assistant_output = api_output.choices[0].message.content

    # Calculate tokens
    completion_tokens += api_output.usage.completion_tokens
    prompt_tokens += api_output.usage.prompt_tokens
    total_tokens += api_output.usage.total_tokens

    # Print assistant_output, and add it to the messages list.
    print(assistant_output)
    messages.append({"role": "assistant", "content": assistant_output})

    # Check chat count limit and output warning.
    chat_count += 1
    if chat_count >= chat_max:
        print(f"You have reached the max amount of chats available! ({chat_max})")

        break
