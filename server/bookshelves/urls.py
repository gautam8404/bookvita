from django.urls import path
from .views import BookShelveALLView, BookShelveUserView, BookShelveModifyView, BookShelveDetailsView

urlpatterns = [
    path('bookshelves/', BookShelveALLView.as_view()),
    path('bookshelves/<str:username>/', BookShelveUserView.as_view()),
    path('bookshelves/<str:username>/<int:bookshelf_id>/', BookShelveDetailsView.as_view()),
    path('bookshelves/<str:username>/<int:bookshelf_id>/modify/', BookShelveModifyView.as_view()),
]