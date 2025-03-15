#TYPING SPEED TESTER
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Artificial intelligence is the future.",
    "Typing speed tests are fun and useful",
    "Never stop learning new things.",
]

sentence = random.choice(sentences)
print("Type the following sentence as quickly as possible:")
print(sentence)


start_time = time.time()
user_input = input("Your turn: ")
end_time = time.time()

time_taken = end_time - start_time
word_count = len(sentence.split())
wpm = (word_count / time_taken)*60

correct_chars = sum(1 for a, b in zip(sentence, user_input) if a ==b)
accuracy = (correct_chars / len(sentence)) * 100


print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Words per minute: {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")

