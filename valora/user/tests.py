# import requests
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Permission, User
# from django.urls import reverse
# from django.test import TestCase
#
#
# # variáveis globais
# adminUsername = 'admintest'
# adminPassword = 'senha123msa'
# adminUserPk = ''
# username = 'usuariotest'
# password = 'senha123msa'
# userPk = ''
# email =  'albertow@email.com'
# Usuario = get_user_model()
#
#
# class UserModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             username='testuser',
#             email='testuser@msaprecodereferencia.com.br',
#             password='user123test',
#             first_name='Test',
#             last_name='User',
#             is_staff=False,
#             is_superuser=False,
#         )
#
#     def test_status_code(self):
#         url = 'http://127.0.0.1:8000/user_create'
#         headers = {
#             'username': username,
#             'email':email,
#             'password1': password,
#             'password2': password,
#         }
#
#         response = requests.get(url, headers=headers)
#         print(response)
#         self.assertEquals(response.status_code, 200)