#####################
'''
Follow the instructions in the text file and run main.py

Enjoy!
To be fleshed out later. Sleep now.

'''
#####################

import os
import openai
import gradio as gr

with open("openai_api_key.txt", "r") as f:
    apiKey = f.read()
    openai.api_key = apiKey
print(f"API key: {apiKey}")

def generate_response(prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty): # generates response from parameters
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens,
      top_p=top_p,
      frequency_penalty=frequency_penalty,
      presence_penalty=presence_penalty
    )
    text = response['choices'][0]['text']
    return text

iface = gr.Interface( # Creates the interface
    fn=generate_response,
    inputs=[
        gr.inputs.Textbox(label="text-davinci-003 prompt"),
        gr.inputs.Slider(label="Temperature (creativity, randomness)", minimum=0.0, maximum=1.0, step=0.1, default=0.7),
        gr.inputs.Slider(label="Max Tokens (length of response, processing power)", minimum=16, maximum=2048, step=16, default=256),
        gr.inputs.Slider(label="Top P (language diversity, 0.5=default)", minimum=0.0, maximum=1.0, step=0.1, default=0.5),
        gr.inputs.Slider(label="Frequency Penalty (decreases repetitiveness)", minimum=0.0, maximum=2.0, step=0.1, default=0.0),
        gr.inputs.Slider(label="Presence Penalty (changes topics)", minimum=0.0, maximum=2.0, step=0.1, default=0.0)
    ],
    outputs=gr.outputs.Textbox(label="Response"),
)

iface.launch(share=True) # Renders the interface