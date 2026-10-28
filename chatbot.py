# ============================================================
# Project: Rule-Based AI Chatbot
# Author:  DecodeLabs Internship - Project 01
# Description: A simple chatbot that uses if-elif-else logic
#              to respond to predefined user inputs.
#              No machine learning or external APIs used.
# ============================================================


def get_response(user_input):
    """
    Takes the user's message, cleans it up, and returns
    an appropriate response based on predefined rules.

    Parameters:
        user_input (str): The raw text typed by the user.

    Returns:
        str: The chatbot's response.
    """

    # --- Step 1: Clean the input ---
    # Convert to lowercase so "Hello" and "hello" are treated the same.
    # Strip removes any leading/trailing spaces the user may have typed.
    message = user_input.lower().strip()

    # --------------------------------------------------------
    # Rule 1: Greetings
    # Handles common ways a user might say hello.
    # --------------------------------------------------------
    if message in ["hello", "hi", "hey", "hello!", "hi!", "hey!"]:
        return "Hello! 👋 Great to see you! How can I help you today?"

    # --------------------------------------------------------
    # Rule 2: How are you?
    # --------------------------------------------------------
    elif message in ["how are you", "how are you?", "how r u", "how r u?"]:
        return "I'm doing great, thanks for asking! 😊 I'm always ready to chat."

    # --------------------------------------------------------
    # Rule 3: What is your name?
    # --------------------------------------------------------
    elif message in ["what is your name", "what is your name?",
                     "what's your name", "what's your name?",
                     "who are you", "who are you?"]:
        return "I'm RuleBot 🤖 — a simple rule-based AI chatbot built with Python!"

    # --------------------------------------------------------
    # Rule 4: What can you do?
    # --------------------------------------------------------
    elif message in ["what can you do", "what can you do?",
                     "what do you do", "what do you do?",
                     "help", "help?"]:
        return (
            "Here's what I can help you with:\n"
            "  • Answer basic questions about myself\n"
            "  • Tell you what AI is\n"
            "  • Have a friendly conversation\n"
            "  • Respond to greetings and farewells\n"
            "Just type your question and I'll do my best! 😊"
        )

    # --------------------------------------------------------
    # Rule 5: What is AI?
    # --------------------------------------------------------
    elif message in ["what is ai", "what is ai?",
                     "what is artificial intelligence",
                     "what is artificial intelligence?",
                     "define ai", "explain ai"]:
        return (
            "AI stands for Artificial Intelligence. 🧠\n"
            "It is the simulation of human intelligence by computer systems.\n"
            "AI can learn, reason, problem-solve, and understand language.\n"
            "Examples include chatbots, voice assistants, and image recognition."
        )

    # --------------------------------------------------------
    # Rule 6: Thank you
    # --------------------------------------------------------
    elif message in ["thank you", "thank you!", "thanks", "thanks!",
                     "thank u", "thx"]:
        return "You're very welcome! 😊 Feel free to ask me anything else."

    # --------------------------------------------------------
    # Rule 7: Asking about the chatbot's creator / project
    # --------------------------------------------------------
    elif message in ["who made you", "who built you", "who created you",
                     "who made you?", "who built you?", "who created you?"]:
        return (
            "I was built as part of DecodeLabs Internship - Project 01! 🚀\n"
            "I'm a rule-based chatbot written entirely in Python."
        )

    # --------------------------------------------------------
    # Rule 8: Time / Date (fun addition for demonstration)
    # --------------------------------------------------------
    elif message in ["what time is it", "what time is it?",
                     "what's the time", "current time"]:
        # We use Python's built-in datetime module — no install needed!
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time on your system is {now} ⏰"

    elif message in ["what is today", "what is today?",
                     "what's the date", "current date", "today's date"]:
        import datetime
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today} 📅"

    # --------------------------------------------------------
    # Rule 9: Farewell — detected here as a fallback check
    # (The main loop handles bye/exit/quit, but we also
    #  catch 'goodbye' and 'see you' as friendly variants)
    # --------------------------------------------------------
    elif message in ["goodbye", "goodbye!", "see you", "see ya",
                     "take care", "later"]:
        return "Goodbye! 👋 It was nice chatting with you. Take care!"

    # --------------------------------------------------------
    # Rule 10: Fallback — unknown input
    # Politely lets the user know the input wasn't understood.
    # --------------------------------------------------------
    else:
        return (
            "Hmm, I'm not sure how to answer that. 🤔\n"
            "Try asking me things like:\n"
            "  → 'What is your name?'\n"
            "  → 'What is AI?'\n"
            "  → 'What can you do?'\n"
            "Type 'help' to see all my capabilities!"
        )


def display_welcome():
    """
    Prints a friendly welcome banner when the chatbot starts.
    This makes the chatbot feel polished and easy to use.
    """
    print("=" * 55)
    print("        Welcome to RuleBot 🤖")
    print("        DecodeLabs Internship — Project 01")
    print("=" * 55)
    print("  I am a simple rule-based AI chatbot.")
    print("  I respond to common questions and greetings.")
    print()
    print("  Try asking me:")
    print("    • Hello / Hi / Hey")
    print("    • How are you?")
    print("    • What is your name?")
    print("    • What can you do?")
    print("    • What is AI?")
    print("    • Thank you")
    print()
    print("  Type  'bye', 'exit', or 'quit'  to stop.")
    print("=" * 55)
    print()


def main():
    """
    The main function that runs the chatbot.

    Flow:
      1. Display the welcome message.
      2. Enter a loop that keeps asking the user for input.
      3. If the user types a farewell word, exit politely.
      4. Otherwise, send the input to get_response() and print the reply.
    """

    # Show the welcome banner
    display_welcome()

    # --- Main loop ---
    # The loop runs forever until the user says bye/exit/quit.
    while True:

        # Prompt the user for input
        user_input = input("You: ")

        # Clean the input once here so we can check for exit commands
        cleaned = user_input.lower().strip()

        # --- Exit condition ---
        # If the user types any farewell keyword, say goodbye and stop.
        if cleaned in ["bye", "exit", "quit", "bye!", "exit!", "quit!"]:
            print("RuleBot: Goodbye! 👋 Thanks for chatting. Have a great day!")
            print("=" * 55)
            break  # Exit the while loop

        # --- Empty input check ---
        # If the user presses Enter without typing anything, nudge them.
        if cleaned == "":
            print("RuleBot: Please type something! I'm listening. 😊")
            print()
            continue  # Skip to the next iteration of the loop

        # --- Get and display the response ---
        response = get_response(user_input)
        print(f"RuleBot: {response}")
        print()  # Blank line for readability between exchanges


# ============================================================
# Entry point — this block runs only when the script is
# executed directly (not when imported as a module).
# ============================================================
if __name__ == "__main__":
    main()
