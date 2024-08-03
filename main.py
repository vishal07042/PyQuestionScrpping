# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")

# res = response.text

# soup = BeautifulSoup(res, "lxml")


# task_list_items = soup.find_all("li", class_="task-list-item")

# # List to store all correct answers
# correct_answers = []

# # Iterate through each list item to find the correct answers
# for item in task_list_items:
#     input_tag = item.find("input", class_="task-list-item-checkbox")
#     if input_tag and input_tag.has_attr("checked"):
#         correct_answer = item.get_text(strip=True)
#         correct_answers.append(correct_answer)

# # Print all correct answers
# for answer in correct_answers:
#     print(f"Correct Answer: {answer}")


# import json
# from bs4 import BeautifulSoup
# import requests

# # Fetch the page content
# response = requests.get(
#     "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
# res = response.text

# # Parse the page content
# soup = BeautifulSoup(res, "lxml")

# # Find all list items with the class "task-list-item"
# task_list_items = soup.find_all("li", class_="task-list-item")

# # List to store all correct answers
# correct_answers = []

# # Iterate through each list item to find the correct answers
# for item in task_list_items:
#     input_tag = item.find("input", class_="task-list-item-checkbox")
#     if input_tag and input_tag.has_attr("checked"):
#         correct_answer = item.get_text(strip=True)
#         correct_answers.append(correct_answer)

# # Load the existing quiz data
# with open('quiz_data.json', 'r') as file:
#     quiz_data = json.load(file)

# # Update the quiz data with the correct answers
# for question in quiz_data:
#     question_id = question['id']
#     if question_id <= len(correct_answers):
#         question['answer'] = correct_answers[question_id - 1]

# # Save the updated quiz data back to the file
# with open('quiz_data.json', 'w') as file:
#     json.dump(quiz_data, file, indent=4)

# # Print all correct answers
# for answer in correct_answers:
#     print(f"Correct Answer: {answer}")


# import json
# from bs4 import BeautifulSoup
# import requests

# # Fetch the page content
# response = requests.get(
#     "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
# res = response.text

# # Parse the page content
# soup = BeautifulSoup(res, "lxml")

# # Find all list items with the class "task-list-item"
# task_list_items = soup.find_all("li", class_="task-list-item")

# # List to store all correct answers
# correct_answers = []

# # Iterate through each list item to find the correct answers
# for item in task_list_items:
#     input_tag = item.find("input", class_="task-list-item-checkbox")
#     if input_tag and input_tag.has_attr("checked"):
#         correct_answer = item.get_text(strip=True)
#         correct_answers.append(correct_answer)

# # Load the existing quiz data
# with open('quiz_data.json', 'r') as file:
#     quiz_data = json.load(file)

# # Update the quiz data with the correct answers
# for question in quiz_data:
#     question_id = question['id']
#     if question_id <= len(correct_answers):
#         question['answer'] = correct_answers[question_id - 1]

# # Save the updated quiz data back to the file
# with open('quiz_data.json', 'w') as file:
#     json.dump(quiz_data, file, indent=4)

# # Print all correct answers
# for answer in correct_answers:
#     print(f"Correct Answer: {answer}")


import json
from bs4 import BeautifulSoup
import requests

# Fetch the page content
response = requests.get(
    "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
res = response.text

# Parse the page content
soup = BeautifulSoup(res, "lxml")

# Find all list items with the class "task-list-item"
task_list_items = soup.find_all("li", class_="task-list-item")

# List to store all correct answers
correct_answers = []

# Iterate through each list item to find the correct answers
for item in task_list_items:
    input_tag = item.find("input", class_="task-list-item-checkbox")
    if input_tag and input_tag.has_attr("checked"):
        correct_answer = item.get_text(strip=True).split(
            '\n')[0]  # Extracting the answer part
        correct_answers.append(correct_answer)

# Load the existing quiz data
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

# Update the quiz data with the correct answers
for question in quiz_data:
    question_id = question['id']
    if question_id <= len(correct_answers):
        # Adjust for 0-indexing
        question['answer'] = correct_answers[question_id - 1]

# Save the updated quiz data back to the file
with open('quiz_data.json', 'w') as file:
    json.dump(quiz_data, file, indent=4)

# Print all correct answers
for answer in correct_answers:
    print(f"Correct Answer: {answer}")
