A simple application of the OpenAI API.
  
#Reasons I use this instead of ChatGPT:
* much faster results
* less censorship
* more control over parameters (more customizeable results)

#Downsides:
* Will require an OpenAI API key (paid after may 1st)
* Must be run once every 3 days to make sure the Gradio server is online (to be hosted on HuggingFace soon)

#Features:
* Fully working Davinci-3 autocompletion model
* Tweakable variables for realtime editing of the model's behavior.
    * Temperature (creativity, randomness)
    * Max Tokens (length of response, processing power)
    * Top P (language diversity, default = 0.5)
    * Frequency Penalty (decreases repetitiveness)
    * Presence Penalty (changes topics more often)
    
