from django.urls import path
from users.views import (
    ProfileView, 
    ProfileEditView, 
    UserLoginView,
    UserLogoutView,
    UserSignupView,
    FollowersListView,
)
app_name = 'users'

urlpatterns = [
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('cadastro/', UserSignupView.as_view(), name='signup'),

    #Actions
    path('follow/<int:pk>/', FollowersListView.as_view(), name='follow'),
]
