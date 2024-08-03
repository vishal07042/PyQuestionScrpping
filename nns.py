# # # import json
# # # from bs4 import BeautifulSoup
# # # import requests

# # # # Fetch the page content
# # # response = requests.get(
# # #     "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
# # # res = response.text

# # # # Parse the page content
# # # soup = BeautifulSoup(res, "lxml")

# # # # Find all list items with the class "task-list-item"
# # # task_list_items = soup.find_all("li", class_="task-list-item")

# # # # List to store all correct answers
# # # correct_answers = []

# # # # Iterate through each list item to find the correct answers
# # # for item in task_list_items:
# # #     input_tag = item.find("input", class_="task-list-item-checkbox")
# # #     if input_tag and input_tag.has_attr("checked"):
# # #         correct_answer_text = item.get_text(strip=True)
# # #         # Assuming option label is the first character
# # #         option_label = correct_answer_text[0]
# # #         # Removing the option label and space
# # #         answer_text = correct_answer_text[3:]
# # #         correct_answers.append((option_label, answer_text))

# # # # Load the existing quiz data
# # # with open('quiz_data.json', 'r') as file:
# # #     quiz_data = json.load(file)

# # # # Update the quiz data with the correct answers
# # # for question in quiz_data:
# # #     question_id = question['id']
# # #     if question_id <= len(correct_answers):
# # #         correct_option, _ = correct_answers[question_id - 1]
# # #         # Find the correct answer in the choices
# # #         for choice in question['choices']:
# # #             if choice.startswith(correct_option):
# # #                 # Update the answer field with formatted text
# # #                 question['answer'] = f"Option {correct_option}: {choice[3:]}"
# # #                 print(f"Updated question {question_id} with answer {
# # #                       question['answer']}")
# # #                 break

# # # # Save the updated quiz data back to the file
# # # with open('quiz_data.json', 'w') as file:
# # #     json.dump(quiz_data, file, indent=4)

# # # # Print all correct answers with option labels
# # # for option, answer in correct_answers:
# # #     print(f"Option {option} is the correct option: {answer}")


# # import json
# # import os
# # from bs4 import BeautifulSoup
# # import requests

# # # Fetch the page content
# # response = requests.get(
# #     "https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
# # res = response.text

# # # Parse the page content
# # soup = BeautifulSoup(res, "lxml")

# # # Find all list items with the class "task-list-item"
# # task_list_items = soup.find_all("li", class_="task-list-item")

# # # List to store all correct answers
# # correct_answers = []

# # # Iterate through each list item to find the correct answers
# # for item in task_list_items:
# #     input_tag = item.find("input", class_="task-list-item-checkbox")
# #     if input_tag and input_tag.has_attr("checked"):
# #         correct_answer_text = item.get_text(strip=True)
# #         # Assuming option label is the first character
# #         option_label = correct_answer_text[0]
# #         # Removing the option label and space
# #         answer_text = correct_answer_text[3:]
# #         correct_answers.append((option_label, answer_text))

# # # Check if the file exists and is not empty
# # if os.path.exists('quiz_data.json') and os.path.getsize('quiz_data.json') > 0:
# #     # Load the existing quiz data
# #     with open('quiz_data.json', 'r') as file:
# #         quiz_data = json.load(file)

# #     # Update the quiz data with the correct answers
# #     for question in quiz_data:
# #         question_id = question['id']
# #         if question_id <= len(correct_answers):
# #             correct_option, _ = correct_answers[question_id - 1]
# #             # Find the correct answer in the choices
# #             for choice in question['choices']:
# #                 if choice.startswith(correct_option):
# #                     # Update the answer field with formatted text
# #                     question['answer'] = f"Option {
# #                         correct_option}: {choice[3:]}"
# #                     print(f"Updated question {question_id} with answer {
# #                           question['answer']}")
# #                     break

# #     # Save the updated quiz data back to the file
# #     with open('quiz_data.json', 'w') as file:
# #         json.dump(quiz_data, file, indent=4)
# # else:
# #     print("quiz_data.json file is missing or empty.")

# # # Print all correct answers with option labels
# # for option, answer in correct_answers:
# #     print(f"Option {option} is the correct option: {answer}")


# import json
# import os
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
#         correct_answer_text = item.get_text(strip=True)
#         # Assuming option label is the first character
#         option_label = correct_answer_text[0]
#         # Removing the option label and space
#         answer_text = correct_answer_text[2:]
#         correct_answers.append((option_label, answer_text))

# # Check if the file exists and is not empty
# if os.path.exists('quiz_data.json') and os.path.getsize('quiz_data.json') > 0:
#     try:
#         # Load the existing quiz data
#         with open('quiz_data.json', 'r') as file:
#             quiz_data = json.load(file)
#         print("Loaded quiz_data.json successfully.")

#         # Update the quiz data with the correct answers
#         for question in quiz_data:
#             question_id = question['id']
#             if question_id <= len(correct_answers):
#                 correct_option, _ = correct_answers[question_id - 1]
#                 for choice in question['choices']:
#                     if choice.startswith(correct_option):
#                         # Adding the option label to the answer
#                         question['answer'] = f"{correct_option}: {choice[3:]}"
#                         print(f"Updated question {question_id} with answer {
#                               question['answer']}")
#                         break

#         # Save the updated quiz data back to the file
#         with open('quiz_data.json', 'w') as file:
#             json.dump(quiz_data, file, indent=4)
#         print("Updated quiz_data.json successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# else:
#     print("quiz_data.json file is missing or empty.")

# # Print all correct answers with option labels
# for option, answer in correct_answers:
#     print(f"Option {option} is the correct option: {answer}")


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
        correct_answer_text = item.get_text(strip=True)
        # Assuming option label is the first character
        option_label = correct_answer_text[0]
        # Removing the option label and space
        answer_text = correct_answer_text[3:]
        correct_answers.append((option_label, answer_text))

# Load the existing quiz data
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

# Update the quiz data with the correct answers
for question in quiz_data:
    question_id = question['id']
    if question_id <= len(correct_answers):
        correct_option, _ = correct_answers[question_id - 1]
        # Find the correct answer in the choices
        for choice in question['choices']:
            if choice.startswith(correct_option):
                # Update the answer field with formatted text
                question['answer'] = f"Option {
                    correct_option} is the correct answer: {choice[3:]}"
                print(f"Updated question {question_id} with answer {
                      question['answer']}")
                break

# Save the updated quiz data back to the file
with open('quiz_data.json', 'w') as file:
    json.dump(quiz_data, file, indent=4)

# Print all correct answers with option labels
for option, answer in correct_answers:
    print(f"Option {option} is the correct option: {answer}")
