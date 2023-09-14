import os
import openai


# Derive API-key from an environment variable.
# How2: Set API-key for Windows: setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")

# OpenAI API Configurations
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"
system_prompt = "You are a voice assistant."

# Chat Variables
chat_messages = []
chat_count = 0
chat_max = 3

# Initialize token variables
total_input_tokens = 0
total_output_tokens = 0
total_token_cost = 0
# Pricing per token
input_token_pricing = 0.0015 / 1000     # Fetched 01.09.23 (openai.com/pricing)
output_token_pricing = 0.002 / 1000     # Fetched 01.09.23 (openai.com/pricing)
currency = "USD"


# Function to prompt model with a list of messages and return the generated response.
def prompt_model(messages):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    
    return (response.choices[0].message.content, response)


# Function to generate an assistant response based on the user's input.
def get_api_response(user_prompt):
    # Add user_prompt to messages list.
    chat_messages.append({"role": "user", "content": user_prompt})

    # Prompt model and get output.
    api_output = prompt_model(chat_messages)[1]
    assistant_text_response = api_output.choices[0].message.content

    # Add assistant output to the messages list.
    chat_messages.append({"role": "assistant", "content": assistant_text_response})

    return api_output

       
# Function to calculate cost from input and output tokens.
def calculate_token_cost(api_output):
    total_input_tokens += api_output.usage.prompt_tokens
    total_output_tokens += api_output.usage.completion_tokens
    token_cost = (total_input_tokens * input_token_pricing) + (total_output_tokens * output_token_pricing)

    return token_cost


# Function to check if the chat_count has exceeded chat_max.
def check_chat_max(chat_max):
    chat_count += 1
    if chat_count >= chat_max:

        print(
            f"You have reached the max amount of chats available! ({chat_max})\n"
            f"This conversation cost {total_token_cost} {currency}"
        )
        return True
