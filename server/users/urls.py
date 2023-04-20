from django.urls import path, include
from .views import UserRegisterView, UserLoginView, is_authenticated, RefreshTokenView, UserLogoutView, UserView, UserDetailView


urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('refresh/', RefreshTokenView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('is-authenticated/', is_authenticated.as_view(), name='is-authenticated'),

    path('users/', UserView.as_view()),
    path('users/<str:username>/', UserDetailView.as_view()),
    path('users/<str:username>/books/', include('track.urls')),

]