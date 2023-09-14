import json
import speech_2_text, text_2_text, text_2_speech


# Get configurations
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    s2t = config["speech_2_text"]
    t2t = config["text_2_text"]
    t2s = config["text_2_speech"]

# Introduction
print(
    f"You are using {text_2_text.model_name}\n"
    f"Max chats is set to {text_2_text.chat_max}"
)

# Append system prompt to the messages list.
text_2_text.chat_messages.append({"role": "system", "content": text_2_text.system_prompt})

while True:
    # Get user speech.
    user_prompt = speech_2_text.speech_2_text(config["speech_2_text"]["api_key"])
    print(f"> {user_prompt}")

    # Get assistant text response by prompting API with user_prompt.
    api_output = text_2_text.get_api_response(t2t["model"], user_prompt)
    assistant_text_response = api_output.choices[0].message.content
    print(assistant_speech_response)

    # Convert assistant_text_response to speech, then output as audio.
    assistant_speech_response = text_2_speech.text2speech(t2s["api_key"], assistant_text_response, t2s["voice"], t2s["model"])
    text_2_speech.output_speech(assistant_speech_response)

    # Calculate tokens used from the API response.
    token_cost = text_2_text.calculate_token_cost(t2t["input_token_cost"], t2t["output_token_cost"], api_output)
    text_2_text.total_token_cost += token_cost

    # Check chat count limit and output warning if it exceeds chat_max.
    if text_2_text.check_chat_max(t2t["chat_max"], t2t["currency"]):
        break
