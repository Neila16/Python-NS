import os
import string

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "task1.txt")

with open(file_path, "r") as file:
    lines = file.readlines()


line_count = len(lines)
word_count = 0
words_freq = {}

for line in lines:
    line = line.lower()
    line = line.translate(str.maketrans("", "", string.punctuation))
    words = line.split()

    word_count += len(words)

    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1

with open("analysis.txt", "w") as file:
    file.write(f"Lines: {line_count}\n")
    file.write(f"Words: {word_count}\n")
    file.write("Word frequency:\n")

    for word, count in words_freq.items():
        file.write(f"{word}: {count}\n")
