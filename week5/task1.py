import os
import string

base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "task1.txt")
output_path = os.path.join(base_dir, "analysis.txt")

with open(input_path, "r") as file:
    lines = file.readlines()

total_lines = len(lines)  
total_words = 0
word_freq = {}

for line in lines:
    line = line.lower().translate(str.maketrans("", "", string.punctuation))
    words = line.split()
    total_words += len(words)
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

with open(output_path, "w") as file:
    file.write(f"Lines: {total_lines}\n")
    file.write(f"Words: {total_words}\n")
    file.write("Word frequency:\n")
    for word, count in word_freq.items():
        file.write(f"{word}: {count}\n")
