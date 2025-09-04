# File Processing Challenge

# Create input.txt with five lines of text
with open("input.txt", "w") as f:
    f.write("Python is fun.\n")
    f.write("Learning to code is useful.\n")
    f.write("Practice makes perfect.\n")
    f.write("Read and write files in Python.\n")
    f.write("This is the fifth line.\n")

# Read contents of input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Count words
word_count = len(content.split())

# Convert to uppercase
upper_content = content.upper()

# Write processed text and word count to output.txt
with open("output.txt", "w") as f:
    f.write(upper_content)
    f.write(f"\nWord count: {word_count}\n")

print("Success! output.txt has been created with processed text and word count.")

