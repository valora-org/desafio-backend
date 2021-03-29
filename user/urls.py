from django.urls import path
from .views import (RegisterPlayerView,
                    RegisterAdminView,
                    AuthenticateUserView,
                    ListUserProfileView,
                    RetrieveUserProfileView,
                    DeleteUserProfileView,
                    UpdateUserProfile,
                    ChangePassUserView,
                    GlobalRankingView,
                    CategoryRankingView)

app_name = "api-user"

urlpatterns = [
    path('register_player', RegisterPlayerView.as_view(), name='register_player'),
    path('register_admin', RegisterAdminView.as_view(), name='register_admin'),
    path('authenticate_user', AuthenticateUserView.as_view(), name='authenticate_user'),
    path('list_user', ListUserProfileView.as_view(), name='list_user'),
    path('retrieve_user/<int:id>', RetrieveUserProfileView.as_view(), name='retrieve_user'),
    path('delete_user/<int:id>', DeleteUserProfileView.as_view(), name='delete_user'),
    path('update_user/<int:id>', UpdateUserProfile.as_view(), name='update_user'),
    path('change_password/<int:id>', ChangePassUserView.as_view(), name='change_password'),
    path('global_ranking', GlobalRankingView.as_view(), name='global_ranking'),
    path('category_ranking/<int:category>', CategoryRankingView.as_view(), name='category_ranking'),
]