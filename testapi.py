import openai

#API_KEY.oh.no = open("API_KEY", "r").read()

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the difference between Celsius and Fahrenheit?"}
    ]
)

print(response)