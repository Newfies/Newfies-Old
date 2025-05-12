import random

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = file.readlines()

# Pick a random quote
quote = random.choice(quotes).strip()

# Read existing README
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.readlines()

# Replace between <!--QUOTE-START--> and <!--QUOTE-END-->
new_readme = []
inside = False
for line in readme:
    if "<!--QUOTE-START-->" in line:
        inside = True
        new_readme.append(line)
        new_readme.append(f"> {quote}\n")
    elif "<!--QUOTE-END-->" in line:
        inside = False
        new_readme.append(line)
    elif not inside:
        new_readme.append(line)

# Save README
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(new_readme)
