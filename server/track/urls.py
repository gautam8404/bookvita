from django.urls import path
from .views import TrackView, TrackDetailsView

urlpatterns = [
    path('', TrackView.as_view()),
    path('<str:book_id>/', TrackDetailsView.as_view()),
]