from openai import OpenAI

#client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
   api_key=("Open AI_API_key"),
 )
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, generally like Alexa Siri and google assistant."},
    {"role": "user", "content":"what is coding"}
  ]
)

print(completion.choices[0].message.content)