from django.urls import path
from .views import BookListView, BookDetailView, BookOLTrending, BookOLSubject, BookOLSearch, ToggleBookLikesView, \
    UserLikesView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<str:book_id>/', BookDetailView.as_view()),
    path('books/<str:book_id>/like/', ToggleBookLikesView.as_view()),
    path('books/<str:username>/liked/', UserLikesView.as_view()),

    path('trending/', BookOLTrending.as_view()),
    path('trending/<str:time>/', BookOLTrending.as_view()),
    path('subject/<str:subject>/', BookOLSubject.as_view()),
    path('search/', BookOLSearch.as_view()),
]
