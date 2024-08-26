from openai import OpenAI
client = OpenAI(
    api_key="YOU_API_KEY"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "YOU_DETAILS_HERE"},
        {
            "role": "user",
            "content": "content"
        }
    ]
)

print(completion.choices[0].message.content)