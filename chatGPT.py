from openai import OpenAI
import openai
import os
# from mistyPy.Robot import Robot

# import speech_recognition as sr
# import pyaudio
import time

# from mistyPy.Events import Events

prompt = open('./openAI_prompt.txt', 'r', encoding="utf8")
prompt = ''.join(prompt.readlines())
# print(prompt)

openai.key=''
client = OpenAI(api_key=openai.key)

# I have confusion I am married lady my husband working in abroad but i luv one person near of my area and I was eager to sex with him.. what can I do pls give ur suggestion

messages = [
  {
    "role": "system", 
    "content": prompt
  }
  ]


while True:
  text = input('User:')
  # misty.stop_speaking()
  # init_rec = sr.Recognizer()
  
  # with sr.Microphone() as source:
  #   audio_data = init_rec.record(source, duration=20)
  #   print("Recognizing your text.............")
  #   text = init_rec.recognize_google(audio_data)
  
  # print('User:', text)
  messages.append({'role': 'user', 'content': text})
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  reply = completion.choices[0].message.content
  messages.append({'role': 'assistant', 'content': reply})
  print('Chatgpt:', reply)
  # misty.speak(reply)



  # time.sleep(5)