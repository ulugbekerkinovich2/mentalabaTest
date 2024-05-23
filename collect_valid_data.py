import json
import time
import requests
from icecream import ic
# from send_req import verify, auth

base_url = "https://testim.mentalaba.uz/v1"
def get_subjects_local(subject=None):
    try:

        with open('subjects.json', 'r', encoding='utf-8-sig') as f:
            subjects = json.load(f)
        
  
        if subject is None and isinstance(subjects, list):
            return subjects
        elif subject is not None:
            for obj in subjects:
                if obj['subject'] == subject:
                    return obj['subject_id']
            return None

            # for obj in dataTest:
                # ic(obj)
                # time.sleep(1)  # Pause for 1 second between each print
        # else:
        #     print("JSON structure is not a list. Please check the JSON structure.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_all_test(subject):
    array = []
    count = 0
    try:
        
        with open('mentalabaTest.json', 'r', encoding='utf-8-sig') as f:
            dataTest = json.load(f)
        
        # all_subjects = get_subjects_local()
        # ic(all_subjects)
        # ic(subject)
        subject_id = get_subjects_local(subject) if subject is not None else None
        # for obj in all_subjects:
        #     if obj['subject'] == subject:
        #         ic(obj['subject'])
        #         subject_id = obj['id']
        #         break
        if subject is not None:
            if isinstance(dataTest, list):
                
                for obj in dataTest:
                    # if count == 30:
                    #     break
                    if obj['Subject_id'] == str(subject_id):
                        if not obj['question_image'].startswith("https") and \
                                not obj['var_a_image'].startswith("https") and \
                                    not obj['var_b_image'].startswith("https") and \
                                        not obj['var_c_image'].startswith("var_d_image") and \
                                            not obj['var_d_image'].startswith("https"):
                            array.append(obj)
                            count += 1
        elif subject is None:
            return False
        return array
        # else:
        #     print("JSON structure is not a list. Please check the JSON structure.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def get_subject_global(token, subject):
    # ic(auth())
    # code = input("Enter code from sms: ")
    # token = verify(int(code))
    url = f"{base_url}/subjects"
    headers = {
        'Authorization': f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for obj in data:
            if obj['name_uz'] == subject:
                return obj['id']
        return None
    
    