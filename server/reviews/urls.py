from django.urls import path
from .views import (
    ReviewListView,
    ReviewCreateView,
    ReviewRUDView,
    ToggleLikeView
)

urlpatterns = [
    path('reviews/', ReviewListView.as_view()),
    path('reviews/book/<str:book_id>/', ReviewCreateView.as_view()),
    path('reviews/<int:review_id>/', ReviewRUDView.as_view(), name='review'),
    path('reviews/<int:review_id>/like/', ToggleLikeView.as_view()),
]