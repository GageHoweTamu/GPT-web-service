A simple application of the OpenAI API.
  
## Why not ChatGPT?
* Much faster results, works when ChatGPT is offline
* Less censorship (bypassed moderation endpoint)
* More control over parameters (more customizeable results)

## Downsides
* Will require an OpenAI API key (paid after may 1st)
* Must be run once every 3 days to make sure the Gradio server is online (to be hosted on HuggingFace soon)

## Features
* Fully working Davinci-3 autocompletion model
* Tweakable variables for realtime editing of the model's behavior.
    * Temperature (creativity, randomness)
    * Max Tokens (length of response, processing power)
    * Top P (language diversity, default = 0.5)
    * Frequency Penalty (decreases repetitiveness)
    * Presence Penalty (changes topics more often)
    
## To be added
* Switching between models (GPT-3.5, etc.)
* Presets that change the parameters for different tasks
