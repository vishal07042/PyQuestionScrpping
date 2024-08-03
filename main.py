# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")

# res = response.text

# soup = BeautifulSoup(res, "lxml")


# optionsAll = soup.find_all('li',  class_='task-list-item')


# for el in optionsAll:
#     print(el.get_text(strip=True))


import json
import requests
from bs4 import BeautifulSoup

# Load the existing quiz data
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

# Fetch the page content
response = requests.get(
    "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
res = response.text

# Parse the page content
soup = BeautifulSoup(res, "lxml")

# Extract all questions and options
questions = soup.find_all('h4')
options = soup.find_all('ul', class_='contains-task-list')

# Debugging: Print the number of questions and options found
print(f"Found {len(questions)} questions and {len(options)} option sets")

# Populate the choices for each question in quiz_data
for idx, option in enumerate(options):
    choices = [li.get_text(strip=True)
               for li in option.find_all('li', class_='task-list-item')]
    if idx < len(quiz_data):
        quiz_data[idx]['choices'] = choices

# Debugging: Print the updated quiz_data to verify choices are being added
for item in quiz_data:
    print(f"Question ID: {item['id']}, Choices: {item['choices']}")

# Output the updated quiz data to the JSON file
with open('quiz_data.json', 'w') as file:
    json.dump(quiz_data, file, indent=4)

# Print the resulting JSON structure
print(json.dumps(quiz_data, indent=4))





