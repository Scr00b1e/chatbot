from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How can I help you today?"
        }
    ]
)

print(completion.choices[0].message.content)