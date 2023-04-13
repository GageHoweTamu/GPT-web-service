import os
import openai


with open("openai_api_key.txt", "r") as f:
    openai_api_key = f.read()
    print(openai_api_key)


#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv(openai_api_key)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="hello!",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

text = response['choices'][0]['text']
print(text)