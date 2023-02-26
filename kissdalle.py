import os
import openai
import webbrowser

# API Key and OS env
API_KEY = 'YOUR_KEY_HERE'
os.environ['OPENAI_Key'] = API_KEY
openai.api_key = os.environ['OPENAI_Key']

# Initial prompt asking for the name
name = input("What is your name? ")  # Ask the user for their name

# Checks if the user entered a name
if name:
    # Display the user's name
    print("Hello, " + name + ", please describe the image you want:")
else:
    # If no name was entered
    print("You didn't enter a name. No formalities? Then just describe the image:")

# The whole deal, prompts each time after a description is entered and then prompts again after the response is given
keep_prompting = True
while keep_prompting:
    prompt = input('> ')
    if prompt == 'quit':
        keep_prompting = False
    else:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",  # Change this to get a lower or higher resolution
        )
        webbrowser.open_new_tab(response['data'][0]['url'])
        print(response['data'][0]['url'])
        print('You can describe another image below:')