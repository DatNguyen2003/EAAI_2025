from openai import OpenAI
import openai
import os

prompt = open('./openAI_prompt.txt', 'r', encoding="utf8")
prompt = ''.join(prompt.readlines())

openai.key='sk-proj-rGjKVLWh2WRqhfhJzouLT3BlbkFJsgmddIT6LAEPx64DciB4'
client = OpenAI(api_key=openai.key)


messages = [
  {
    "role": "system", 
    "content": prompt
  }
  ]

# Create the initial message to start the game
print('ChatGPT: Let\'s play the Chameleon game! What is the secret keyword?')

while True:
  text = input('User:')
  
  # print('User:', text)
  messages.append({'role': 'user', 'content': text})
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  reply = completion.choices[0].message.content
  messages.append({'role': 'assistant', 'content': reply})
  print('Chatgpt:', reply)
  result = input('User (win/lost): ')
  messages.append({'role': 'user', 'content': result})
    
  # Acknowledge the result
  if result.lower() == 'win':
      print('ChatGPT: Good')
  elif result.lower() == 'lost':
      print('ChatGPT: Bad')
  else:
      print('ChatGPT: Invalid input, please enter "win" or "lost".')
  
  # Append the assistant's response to the messages list
  messages.append({'role': 'assistant', 'content': reply})
  
  # Optionally, save the conversation to a file
  with open('./openAI_prompt.txt', 'w') as file:
      for message in messages:
          file.write(f"{message['role']}: {message['content']}\n")
  
  # Optionally, break the loop if a certain condition is met (e.g., user says "bye")
  if text.lower() in ["bye", "exit", "quit"]:
      break


    
    
