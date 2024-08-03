

from bs4 import BeautifulSoup
import requests

response = requests.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/node.js/node.js-quiz.md")

res = response.text

soup = BeautifulSoup(res, "lxml")

# ############## the   sarre Questions toh aa agyi #############

res2 = soup.find_all("h4")



# for el in res2:
#     print(el.string) 


 
    
    
    
############# sarre options bhi aageyi aa agyi #############


# optionsAll = soup.find_all('li',  class_='task-list-item')


# for el in optionsAll:
#     print(el.get_text(strip=True))
    
    
############# sarre options bhi aageyi aa agyi #############





############# the options  corrected Form #############


task_list_items = soup.find_all("li", class_="task-list-item")

# List to store all correct answers
correct_answers = []

# Iterate through each list item to find the correct answers
for item in task_list_items:
    input_tag = item.find("input", class_="task-list-item-checkbox")
    if input_tag and input_tag.has_attr("checked"):
        correct_answer = item.get_text(strip=True)
        correct_answers.append(correct_answer)

# Print all correct answers
for answer in correct_answers:
    print(f"Correct Answer: {answer}")



############# the options  corrected Form  hhhelo final#############








  
