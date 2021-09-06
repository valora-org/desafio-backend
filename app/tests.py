import requests

def get_token():
    url = "http://127.0.0.1:8000/api/token/"

    payload = {
        "username": "bruno",
        "password": "bruno@12345"
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()


token = get_token()
headers = {"Authorization": f"Bearer {token['access']}"}

class TestCategory:

    def test_get_category_player(self):
        
        url = "http://127.0.0.1:8000/api/v1/categories/de53151d-8046-4188-8799-626e986ab3b2/"

        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)

        assert response.status_code == 403
    
    def test_get_list_category_player(self):

        url = "http://127.0.0.1:8000/api/v1/categories/"

        payload = ""
        
        response = requests.request("GET", url, data=payload, headers=headers)

        assert response.status_code == 200

class TestQuiz:

    def test_get_quiz_complet_player(self):
        url = "http://127.0.0.1:8000/api/v1/quiz/category/de53151d-8046-4188-8799-626e986ab3b2/"
        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)

        assert response.status_code == 200
    
    def test_get_quiz_incomplet_player_status_code(self):
        url = "http://127.0.0.1:8000/api/v1/quiz/category/99cd235f-e77c-47d5-8d90-fd512475d6a3/"
        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)
        assert response.status_code == 500
    
    def test_get_quiz_incomplet_player_msg(self):
        url = "http://127.0.0.1:8000/api/v1/quiz/category/99cd235f-e77c-47d5-8d90-fd512475d6a3/"
        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)
        response_json = response.json()
        assert response_json['msg'] == (
            'Quiz ainda não possui perguntas sufucientes.'
        )

