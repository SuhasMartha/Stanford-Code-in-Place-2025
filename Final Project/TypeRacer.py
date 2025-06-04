import time
import random
import os

# --- Sentence Lists by Level ---
easy_sentences = [
    "Python is fun",
    "Keep calm and code on",
    "I love to type fast",
    "AI is the future",
    "Hello world",
    "Typing games are fun",
    "Code and coffee",
    "Speed typing is awesome",
    "Learning to code is cool",
    "Be kind and code well",
    "I am learning at Code in Place",
    "Typing is a useful skill",
    "Never give up",
    "Small steps lead to big results",
    "Practice typing daily",
]

medium_sentences = [
    "Code every day to improve your skills.",
    "Practice makes a programmer perfect.",
    "Debugging is twice as hard as writing the code.",
    "Readability counts in Python.",
    "Typing faster helps in coding competitions.",
    "Indentation is important in Python.",
    "You can solve any problem step by step.",
    "Always keep learning and coding.",
    "Write code that makes sense.",
    "Clear code is better than clever code.",
    "Great coders read more than they write.",
    "Think before you type.",
    "Focus on logic, not just syntax.",
    "Consistency builds excellence.",
    "Errors are opportunities to learn."
]

hard_sentences = [
    "Programs must be written for people to read, and only incidentally for machines to execute.",
    "Simplicity is the soul of efficiency, and clean code reflects that.",
    "Premature optimization is the root of all evil in programming.",
    "In programming, the hard part isn’t solving problems, but deciding what problems to solve.",
    "When debugging, novices insert code, experts remove it.",
    "Always code as if the person who ends up maintaining your code is a violent psychopath.",
    "Complexity is the enemy of execution.",
    "Good software is like a garden — it needs constant care.",
    "Readability trumps brevity in production environments.",
    "Name variables like you’re naming your first-born child."
]

# --- Fun facts, quotes, tips ---
fun_facts = [
    "💡 Fun Fact: The first computer programmer was Ada Lovelace in the 1800s!",
    "😂 Tip: Coding is like humor. If you have to explain it, it’s bad.",
    "🚀 Motivation: Keep calm and keep typing fast!",
    "😅 Why do programmers prefer dark mode? Because light attracts bugs!",
    "🌟 Tip: Every great developer started where you are now!",
    "✨ Motivation: Don't worry about being slow. Worry about not improving.",
    "🤖 Fun Fact: The first “Hello, World” program appeared in 1972!",
    "🏁 Tip: Typing is just a race with yourself. Beat your last score!",
    "💻 Motivation: You're doing amazing. One sentence at a time.",
    "📚 Tip: The best way to learn coding is by doing. Keep doing this!",
]

# -- Sentence Manager --
class SentenceManager:
    def __init__(self):
        self.used_easy = set()
        self.used_medium = set()
        self.used_hard = set()

    def get_sentence(self, level):
        if level == '1':
            pool, used = easy_sentences, self.used_easy
        elif level == '2':
            pool, used = medium_sentences, self.used_medium
        else:
            pool, used = hard_sentences, self.used_hard

        available = [s for s in pool if s not in used]
        if not available:
            used.clear()
            available = pool.copy()
        sentence = random.choice(available)
        used.add(sentence)
        return sentence

sentence_manager = SentenceManager()

# -- Score Calculation --
def calculate_results(original, typed, start, end):
    time_taken = round(end - start, 2)
    correct_chars = sum(1 for i, c in enumerate(typed) if i < len(original) and c == original[i])
    accuracy = (correct_chars / len(original)) * 100 if len(original) > 0 else 0
    words_typed = len(typed.split())
    wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0
    return time_taken, accuracy, wpm

def highlight_mistakes(original, typed):
    marks = ""
    length = max(len(original), len(typed))
    for i in range(length):
        o_char = original[i] if i < len(original) else ""
        t_char = typed[i] if i < len(typed) else ""
        marks += " " if o_char == t_char else "^"
    return marks

def get_feedback(accuracy):
    if accuracy >= 95:
        return "🌟 Excellent accuracy! You're a pro!"
    elif accuracy >= 80:
        return "👍 Good typing! Just a bit more precision!"
    else:
        return "🧐 Keep practicing! Accuracy improves with time."

def countdown():
    print("Get ready...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!")

# -- Main Game --
def typing_game():
    print("🎮 Welcome to the Typing Speed Game!")
    name = input("Enter your name: ").strip() or "Player"

    best_wpm = 0.0
    best_accuracy = 0.0
    rounds_played = 0

    while True:
        print("\n🎯 Choose Difficulty Level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        level = input("Enter level (1/2/3): ").strip()
        if level not in ['1', '2', '3']:
            print("⚠️ Invalid input. Defaulting to Easy.")
            level = '1'

        sentence = sentence_manager.get_sentence(level)
        print("\n📝 Type this sentence exactly as shown:")
        print(f"\n\"{sentence}\"\n")

        countdown()
        start = time.time()
        typed = input("Start typing:\n")
        end = time.time()

        time_taken, accuracy, wpm = calculate_results(sentence, typed, start, end)
        best_wpm = max(best_wpm, wpm)
        best_accuracy = max(best_accuracy, accuracy)
        rounds_played += 1

        print("\n✅ Round Summary:")
        print(f"⏱️ Time Taken     : {time_taken:.2f} seconds")
        print(f"🎯 Accuracy       : {accuracy:.2f}%")
        print(f"🚀 WPM            : {wpm:.2f}")
        print(f"🌟 Best WPM       : {best_wpm:.2f}")
        print(f"🎯 Best Accuracy  : {best_accuracy:.2f}%")
        print(f"🔁 Rounds Played  : {rounds_played}")
        print("\nYour result:")
        print(sentence)
        print(highlight_mistakes(sentence, typed))
        print(get_feedback(accuracy))

        print("\n💬 Tip or Fun Fact:")
        print(random.choice(fun_facts))

        again = input("\n🎮 Play another round? (y/n): ").strip().lower()
        if again != 'y':
            break

    print(f"\n👋 Thanks for playing, {name}!")
    print(f"🏁 Final Stats — Rounds Played: {rounds_played}")
    print(f"🚀 Best WPM: {best_wpm:.2f}")
    print(f"🎯 Best Accuracy: {best_accuracy:.2f}%")

if __name__ == "__main__":
    typing_game()
