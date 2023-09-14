import speech_2_text, gpt, text_2_speech


# Introduction
print(
    f"You are using {gpt.model_name}\n"
    f"Max chats is set to {gpt.chat_max}"
)

# Append system prompt to the messages list.
gpt.chat_messages.append({"role": "system", "content": gpt.system_prompt})

while True:
    # Get user speech.
    user_prompt = speech_2_text.speech_2_text()
    print(f"> {user_prompt}")

    # Get assistant text response by prompting API with user_prompt.
    api_output = gpt.get_api_response(user_prompt)
    assistant_text_response = api_output.choices[0].message.content
    print(assistant_speech_response)

    # Convert assistant_text_response to speech, then output as audio.
    assistant_speech_response = text_2_speech.text2speech(assistant_text_response)
    text_2_speech.output_speech(assistant_speech_response)

    # Calculate tokens used from the API response.
    token_cost = gpt.calculate_token_cost(api_output)
    gpt.total_token_cost += token_cost

    # Check chat count limit and output warning if it exceeds chat_max.
    if gpt.check_chat_max(gpt.chat_max):
        break
