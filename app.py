from send_req import create_question
from collect_valid_data import get_all_test, get_subjects_local, get_subject_global
from icecream import ic
import datetime
import json
import time
# from token import token_
token_ = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTA2OTgsImZpcnN0X25hbWUiOiJVbHVnJ2JlayIsImxhc3RfbmFtZSI6IkVya2lub3YiLCJwaG9uZSI6Iis5OTg5NDI1NTkwMTUiLCJlbWFpbCI6InVsdWdiZWs5MDE1dEBnbWFpbC5jb20iLCJhdmF0YXIiOm51bGwsInJvbGUiOiJzdXBlcl9hZG1pbiIsImlzX3ZlcmlmeSI6dHJ1ZSwiY3JlYXRlZF9hdCI6IjIwMjQtMDEtMDVUMTA6NDE6MDIuNDQwWiIsInVwZGF0ZWRfYXQiOiIyMDI0LTAxLTA1VDEwOjQxOjAyLjQ0MFoiLCJzdGF0dXMiOiJzZW50X3NtcyIsInVuaXZlcnNpdHkiOm51bGwsInVuaXZlcnNpdHlfaWQiOm51bGwsInNyYyI6bnVsbCwiaWF0IjoxNzE2NDYzNzUxLCJleHAiOjE3MTY2Nzk3NTF9.US3_HUcr3A7Pd4xu0bRqBmc9XkZrl7e2t_e8ZzJQnyA"
def time_local():
    local_time = datetime.datetime.now()

    # Print just the local time
    return str(local_time.strftime("%H_%M_%S"))
ic(time_local())
with open('unique_test.json', 'r', encoding='utf-8-sig') as f:
    data_unique = json.load(f)

with open('unique_test_biologiya.json', 'r', encoding='utf-8-sig') as f:
    data_unique = json.load(f)
# auth = auth()
# ic(auth)
# code = input("Enter code from sms: ")
# token_ = verify(int(code))

subject_name_math = "Matematika"

subject_name_physic = "Fizika"

subject_name_history = "Tarix"
subject_name_mother_lang = "Ona tili"
subject_name_mother_lang_global = "Ona tili va adabiyoti"
subject_name = "Biologiya"
Kimyo= "Kimyo"
Ingliz_tili = 'Ingliz tili'

subject_id_ = get_subject_global(token_, subject_name_history)
ic(subject_id_)
all_test = get_all_test(subject_name_history)
ic(all_test)

my_time = time_local()
array_res = []
count = 0
for obj in all_test:
    
    if count == 10:
        count = 0
        break

    question_text_ = obj['question']
    var_a = obj['var_a']
    var_b = obj['var_b']
    var_c = obj['var_c']
    var_d = obj['var_d']
    correct_answer = obj['answer']
    variant_id_ = 37

    obj = {
        'question_text': question_text_,
        }

    if obj not in data_unique:
        data_unique.append(obj)
        data, create_question_res = create_question(
            token=token_,
            subject_id=subject_id_,
            question_text=question_text_,
            var1=var_a,
            var2=var_b,
            var3=var_c,
            var4=var_d,
            variant_id=variant_id_,
            correct_answer=correct_answer
        )
        ic(create_question_res)
        count += 1


        array_res.append({"data1": data, 'res': create_question_res})
        with open(f'{my_time}.json', 'w', encoding='utf-8-sig') as f:
            json.dump(array_res, f, ensure_ascii=False, indent=4)

        with open('json/unique_test_DTM_math.json', 'w', encoding='utf-8-sig') as f:
            json.dump(data_unique, f, ensure_ascii=False, indent=4)
    time.sleep(0.1)
