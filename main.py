import speech_recognition as sr   
import pyttsx3
import webbrowser
import musicLibrary
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API keys
api_key_1 = os.getenv('API_KEY_1')
api_key_2 = os.getenv('API_KEY_2')

# Use the API keys
#print(f"API Key 1: {api_key_1}")
#print(f"API Key 2: {api_key_2}")

recognizer = sr.Recognizer()
engine= pyttsx3.init()
                 

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(command):
    client = OpenAI(api_key=(api_key_2),
   
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, generally like Alexa Siri and google assistant."},
        {"role": "user", "content":command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://facebook.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "open linkedin" in c.lower():
        webbrowser.open('https://linkedin.com')
    


    elif "open github" in c.lower():
        webbrowser.open('https://github.com')
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif  "news" in c.lower():
        
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key_1}")
        if r.status_code == 200:
        # Parse the JSON response
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    
    elif "thanks" in c.lower():
        speak("welcome .... Glad to Serve You")
        exit(0)
    else:
        output= aiprocess(c)
        speak(output)
if __name__ == "__main__":
    speak("Initialization jarvis....")  
    while True:
        r = sr.Recognizer()
        print("recoginizing")

        
        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
                
            word = r.recognize_google(audio)
           
        
            if (word.lower()== "jarvis"):
                speak(f"yes sir")
                with sr.Microphone() as source:
                    print('Jarvis Activate....')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
    
        
        except Exception as e:
            print("Jarvis error; {0}".format(e))
