from ollama import chat

with open("data.txt", "r", encoding="utf-8") as f:
    ss_context = f.read()

messages = [
    {
        "role": "system",
        "content": f"""
You are a helpful assistant.

Use ONLY the information below to answer questions.

If the answer isn't in the document, say:
"I couldn't find that in the document."

DOCUMENT:
{ss_context}
""",
    }
]

print("Bot: Ready! Type 'q' to quit.\n")


while True:
    user = input("You: ")

    if user.lower() == "q":
        break

    messages.append({"role": "user", "content": user})

    response = chat(
        model="qwen2.5:0.5b",
        messages=messages,
    )

    reply = response["message"]["content"]
    print(f"\nBot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
