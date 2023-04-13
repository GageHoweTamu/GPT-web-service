import openai
import gradio as gr

#with open('api_key.txt', 'r') as f:
#    openai.api_key = f.read().strip()

openai.api_key = input("please input your API key")

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="https://github.com/GageHoweTamu",
             description="GPT3.5 terminal",
             theme="compact").launch(share=True)

# pathname /Users/gagehowe/Downloads/gptApp.py


'''
to use:
insert your API key into line 4
copy file path
run "python <file path> in os terminal
inspired by https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/
'''
