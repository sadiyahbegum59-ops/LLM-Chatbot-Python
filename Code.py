from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant for students. Answer clearly and briefly."
    }
]

while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        print("Chat ended.")
        break

    messages.append({"role": "user", "content": msg})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})
