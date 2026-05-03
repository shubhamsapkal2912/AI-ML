def ai_chatbot():
    print("AI Chatbot: Hello! Ask me anything about Artificial Intelligence.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        if "what is ai" in user_input:
            print("Bot: AI (Artificial Intelligence) is the simulation of human intelligence in machines.")
        
        elif "types of ai" in user_input:
            print("Bot: The main types are Narrow AI, General AI, and Super AI.")
        
        elif "machine learning" in user_input:
            print("Bot: Machine Learning is a subset of AI that allows systems to learn from data.")
        
        elif "deep learning" in user_input:
            print("Bot: Deep Learning is a subset of Machine Learning using neural networks.")
        
        elif "nlp" in user_input or "natural language processing" in user_input:
            print("Bot: NLP is a field of AI that enables machines to understand human language.")
        
        elif "applications of ai" in user_input:
            print("Bot: AI is used in healthcare, finance, robotics, education, and more.")
        
        elif "turing test" in user_input:
            print("Bot: The Turing Test checks if a machine can mimic human intelligence.")
        
        elif "expert system" in user_input:
            print("Bot: An expert system is AI that mimics decision-making of a human expert.")
        
        elif "robotics" in user_input:
            print("Bot: Robotics is a branch of AI focused on designing intelligent machines.")
        
        elif "advantages of ai" in user_input:
            print("Bot: AI improves efficiency, accuracy, and automation.")
        
        elif "exit" in user_input:
            print("Bot: Goodbye! Keep learning AI 😊")
            break
        
        else:
            print("Bot: Sorry, I don't understand. Please ask AI-related questions.")

ai_chatbot()