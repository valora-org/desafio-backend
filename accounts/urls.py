from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='list-create-account'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path(
        '<str:id>/',
        views.AccountDetailView.as_view(),
        name='account-detail',
    ),
]
