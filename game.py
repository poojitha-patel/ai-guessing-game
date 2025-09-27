from openai import OpenAI

# Initialize OpenAI client (make sure you set OPENAI_API_KEY as an environment variable)
client = OpenAI()

def ai_guessing_game():
    print("🤖 Welcome to the AI Guessing Game!")
    print("Think of an object (e.g., cat, phone, pizza)... I will try to guess it by asking questions.")
    print("Answer with 'yes' or 'no'. Type 'quit' to stop.\n")

    conversation = [
        {"role": "system", "content": "You are playing a 20-questions style game. "
                                      "Ask the user yes/no questions to guess their object. "
                                      "Only ask one question at a time."}
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # lightweight and fast
            messages=conversation,
            max_tokens=50
        )

        ai_message = response.choices[0].message.content
        print("AI:", ai_message)

        user_input = input("You: ").strip().lower()
        if user_input == "quit":
            print("Game ended. Thanks for playing!")
            break

        # Add user input to the conversation
        conversation.append({"role": "assistant", "content": ai_message})
        conversation.append({"role": "user", "content": user_input})

# Run the game
if __name__ == "__main__":
    ai_guessing_game()
