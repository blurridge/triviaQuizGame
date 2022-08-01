# Data

import requests
import json

def get_questions_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        questions_list = list()
        data = json.loads(response.text)
        for i in range(0, len(data['results'])):
            q = ((data['results'][i]['question'].replace("&quot;", "\"")).replace("&rsquo;", "\'")).replace("&#039;", "\'")
            a = ((data['results'][i]['correct_answer'].replace("&quot;", "\"")).replace("&rsquo;", "\'")).replace("&#039;", "\'")
            curr_q = {"text": q, "answer": a}
            questions_list.append(curr_q)
        return questions_list 
    else:
        print("ERROR: Cannot parse questions. Connect to the internet.")
        return None

question_data = get_questions_from_api("https://opentdb.com/api.php?amount=20&difficulty=medium&type=boolean")