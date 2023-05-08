from django.urls import path
from .views import BookShelveALLView, BookShelveUserView, BookShelveModifyView, BookShelveDetailsView,\
    ToggleShelfLikeView, BookShelveLikedView

urlpatterns = [
    path('bookshelves/', BookShelveALLView.as_view()),
    path('bookshelves/<str:username>/', BookShelveUserView.as_view()),
    path('bookshelves/<str:username>/<str:bookshelf_id>/', BookShelveDetailsView.as_view()),
    path('bookshelves/<str:username>/<str:bookshelf_id>/modify/', BookShelveModifyView.as_view()),
    path('bookshelves/<str:username>/<str:bookshelf_id>/like/', ToggleShelfLikeView.as_view()),
    path('bookshelves/<str:username>/liked/', BookShelveLikedView.as_view()),
]