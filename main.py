

# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")

# res = response.text

# soup = BeautifulSoup(res, "lxml")

# # ############## the   sarre Questions toh aa agyi #############

# res2 = soup.find_all("h4")



# # for el in res2:
# #     print(el.string) 


 
    
    
    
# ############# sarre options bhi aageyi aa agyi #############


# # optionsAll = soup.find_all('li',  class_='task-list-item')


# # for el in optionsAll:
# #     print(el.get_text(strip=True))
    
    
# ############# sarre options bhi aageyi aa agyi #############





# ############# the options  corrected Form #############


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



# ############# the options  corrected Form  hhhelo final#############












import json
from bs4 import BeautifulSoup
import requests

response = requests.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")
res = response.text

soup = BeautifulSoup(res, "lxml")

# Debug: Print the fetched content
# print(soup.prettify())

# Find all questions
questions = soup.find_all("h4")

# Debug: Print the number of questions found
print(f"Number of questions found: {len(questions)}")

# List to store all questions, choices, and correct answers
quiz_data = []

# Iterate through each question and its corresponding options
for question in questions:
    question_text = question.get_text(strip=True)
    choices = []
    correct_answer = None
    
    # Debug: Print the question text
    print(f"Question: {question_text}")
    
    # Find the next sibling elements that are options
    next_sibling = question.find_next_sibling()
    while next_sibling and next_sibling.name == "ul":
        for option in next_sibling.find_all("li", class_="task-list-item"):
            option_text = option.get_text(strip=True)
            choices.append(option_text)
            input_tag = option.find("input", class_="task-list-item-checkbox")
            if input_tag and input_tag.has_attr("checked"):
                correct_answer = option_text
        next_sibling = next_sibling.find_next_sibling()
    
    # Debug: Print the choices and correct answer
    print(f"Choices: {choices}")
    print(f"Correct Answer: {correct_answer}")
    
    # Append the question, choices, and correct answer to the list
    quiz_data.append({
        "question": question_text,
        "choices": choices,
        "answer": correct_answer
    })

# Write the formatted quiz data to a JSON file
with open("quiz_data.json", "w", encoding="utf-8") as json_file:
    json.dump(quiz_data, json_file, ensure_ascii=False, indent=4)

print("Quiz data has been written to quiz_data.json")


  


