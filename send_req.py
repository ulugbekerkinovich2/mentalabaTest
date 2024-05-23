import requests
import json
from tqdm import tqdm
from icecream import ic
from mentoken import token
# from collect_valid_data import get_all_test

base_url = "https://testim.mentalaba.uz/v1"

# def auth():
#     url = "https://api.mentalaba.uz/v1/auth/super-admin/login"
#     data = {
#         "email": "ulugbek9015t@gmail.com",
#         "password": "QsD45123"
#     }
#     response = requests.post(url, json=data)
#     if response.status_code == 200:
#         res = response.json()
#         return res.get('status')
    
# def verify(code):
#     url = "https://api.mentalaba.uz/v1/auth/super-admin/verify-login"
#     data = {
#         "email": "ulugbek9015t@gmail.com",
#         "code": code
#     }
#     response = requests.post(url, json=data)
#     ic(response)
#     ic(response.json())
#     if response.status_code == 200:
#         token = response.json()
#         token = token.get('token')
#         return token
#     else:
#         return False
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTA2OTgsImZpcnN0X25hbWUiOiJVbHVnJ2JlayIsImxhc3RfbmFtZSI6IkVya2lub3YiLCJwaG9uZSI6Iis5OTg5NDI1NTkwMTUiLCJlbWFpbCI6InVsdWdiZWs5MDE1dEBnbWFpbC5jb20iLCJhdmF0YXIiOm51bGwsInJvbGUiOiJzdXBlcl9hZG1pbiIsImlzX3ZlcmlmeSI6dHJ1ZSwiY3JlYXRlZF9hdCI6IjIwMjQtMDEtMDVUMTA6NDE6MDIuNDQwWiIsInVwZGF0ZWRfYXQiOiIyMDI0LTAxLTA1VDEwOjQxOjAyLjQ0MFoiLCJzdGF0dXMiOiJzZW50X3NtcyIsInVuaXZlcnNpdHkiOm51bGwsInVuaXZlcnNpdHlfaWQiOm51bGwsInNyYyI6bnVsbCwiaWF0IjoxNzE2NDYzNzUxLCJleHAiOjE3MTY2Nzk3NTF9.US3_HUcr3A7Pd4xu0bRqBmc9XkZrl7e2t_e8ZzJQnyA"

def create_question(token,subject_id,question_text,
                    var1,var2,var3,var4,
                    correct_answer,variant_id):
    # subject_id = get_subjects(subject)
    if subject_id is not None:
        url = f"{base_url}/questions"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        data = {
            "questions": [
                {
                    "subject_id": subject_id,
                    "question": question_text,
                    "options": [
                        var1,
                        var2,
                        var3,
                        var4
                    ],
                    "answer": correct_answer,
                    "variant_id": variant_id,
                    "is_mandatory_subject_question": True
                }
            ]
        }
        ic(data)
        response = requests.post(url, json=data, headers=headers)
        return data, response.json()
    else:
        ic('xatolik yuz berdi subject_id topilmadi')





