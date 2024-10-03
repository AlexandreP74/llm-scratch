import re

with open("resources/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text[:99])
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed)