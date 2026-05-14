def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    print("Sending messages...\n")

    while (len(messages) > 0):
        message = messages.pop(0)
        sent_messages.append(message)
        print(message)


messages: list[str] = ["Message 1", "Message 2", "Message 3"]
sent_messages: list[str] = []

send_messages(messages, sent_messages)

print(f"\n{messages}\n")
print(f"{sent_messages}")
