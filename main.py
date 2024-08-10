import json
import requests
from bs4 import BeautifulSoup

# Load the existing quiz data
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

# Fetch the page content
response = requests.get(
    "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md")
res = response.text

# Parse the page content
soup = BeautifulSoup(res, "lxml")

# Extract all questions and options
questions = soup.find_all('h4')
options = soup.find_all('ul', class_='contains-task-list')

# List to store all correct answers
correct_answers = []

# Extract all task list items
task_list_items = soup.find_all("li", class_="task-list-item")

# Iterate through each list item to find the correct answers
for item in task_list_items:
    input_tag = item.find("input", class_="task-list-item-checkbox")
    if input_tag and input_tag.has_attr("checked"):
        correct_answer = item.get_text(strip=True)
        correct_answers.append(correct_answer)

# Check if the number of questions matches the number of options
if len(questions) != len(options):
    print("Warning: The number of questions and options do not match.")

# Populate the choices and correct answer for each question in quiz_data
for idx, (question, option) in enumerate(zip(questions, options)):
    choices_elements = option.find_all('li', class_='task-list-item')
    choices = [
        f"{chr(65 + i)}: {choice.get_text(strip=True)}"
        for i, choice in enumerate(choices_elements)
    ]
    if idx < len(quiz_data):
        quiz_data[idx]['question'] = question.get_text(strip=True)
        quiz_data[idx]['choices'] = choices
        # Find the correct answer index
        correct_answer = next(
            (choice for choice in choices_elements if choice.get_text(strip=True) in correct_answers), None)
        if correct_answer:
            quiz_data[idx]['answer'] = correct_answer.get_text(strip=True)

# Output the updated quiz data to the JSON file
with open('quiz_data.json', 'w') as file:
    json.dump(quiz_data, file, indent=4)

# Print the resulting JSON structure
print(json.dumps(quiz_data, indent=4))

# Debugging: Print a few questions, their choices, and the correct answer
for i in range(min(5, len(questions))):
    print(f"Question {i+1}: {quiz_data[i]['question']}")
    print(f"Choices: {quiz_data[i]['choices']}")
    print(f"Correct Answer: {quiz_data[i].get('answer', 'No correct answer available')}")