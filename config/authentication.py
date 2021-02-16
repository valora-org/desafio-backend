from rest_framework import authentication as auth


class TokenAuthentication(auth.TokenAuthentication):
    keyword = 'Bearer'
