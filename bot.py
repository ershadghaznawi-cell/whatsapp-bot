from neonize.client import NewClient

def message_handler(client, message):
    print(f"نوی پیغام راورسید: {message}")

client = NewClient("whatsapp_session")

@client.on_message
def handle_incoming_message(client, message):
    message_handler(client, message)

if __name__ == "__main__":
    print("ربات پیل شو، مهرباني وکړئ د QR کوډ سکن کړئ...")
    client.connect()
