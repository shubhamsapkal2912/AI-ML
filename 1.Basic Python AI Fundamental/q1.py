def chatbot():
    print("Simple Chatbot (type 'bye' to exit)")
    
    while True:
        msg = input("You: ").lower()
        
        if msg == "hello":
            print("Bot: Hi! How can I help you?")
        
        elif msg == "how are you":
            print("Bot: I am fine, thank you!")
        
        elif msg == "what is your name":
            print("Bot: I am a simple chatbot.")
        
        elif msg == "bye":
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: Sorry, I don't understand.")


# Run chatbot
chatbot()