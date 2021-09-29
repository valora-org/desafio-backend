import requests

URL_BASE = 'http://localhost:8000/api'

endpoints = {
    'LOGIN': URL_BASE + '/token/',
    'CATEGORY': URL_BASE + '/category/',
    'QUESTION': URL_BASE + '/question/',
    'QUIZ': URL_BASE + '/quiz/',
    'USER': URL_BASE + '/user/',
}


class InsertData(object):
    def __init__(self):
        self.user = None
        self.category = None
        self.token = None
        self.api_authentication()
        self.category = self.create_category()
        self.create_questions()

    def api_authentication(self):
        url = endpoints['LOGIN']
        data = {
            "username": "admin@gmail.com",
            "password": "Pass.123"
        }
        response = requests.post(url, data=data)
        print(f"authentication: {response.status_code}")
        json_response = response.json()
        self.token = "Bearer " + json_response['access']

    def create_category(self):
        category_list = [{"description": "Musica"},
                         {"description": "Educação"},
                         {"description": "Historia"}]
        responses = []
        for item in category_list:
            response = requests.post(url=endpoints['CATEGORY'],
                                     data=item,
                                     headers={"Authorization": self.token})
            responses.append(response.json())
            print(f"create_category : {response.status_code}")
        return responses

    def create_questions(self):
        for cat in self.category:
            data = {"category": cat['id']}
            questions = list()
            for item in range(1, 100):
                questions.append({"question": f"Pergunta {item} - Categoria {cat['description']}",
                                  "answer": [
                                      {"answer": f"Responsta {anw+1} "
                                                 f"Pergunta {item} - "
                                                 f"Categoria {cat['id']} {cat['description']}",
                                       "is_right": True if anw == 0 else False}
                                      for anw in range(0, 3)]
                                  })
            data.update({"question": questions})
            response = requests.post(url=endpoints['QUESTION'],
                                     json=data,
                                     headers={"Authorization": self.token})
            print(f"create_question: {response.status_code}")


if __name__ == '__main__':
    InsertData()
