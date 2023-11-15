from django.urls import path
from book.views import home, storebook, showBook, editBook, deleteBook

urlpatterns = [
    path('',home),
    path('store_book/',storebook,name='storebook'),
    path('show_book/',showBook,name='showbook'),
    path('edit_book/<int:id>',editBook,name='edit_book'),
    path('delete_book/<int:id>',deleteBook,name='delete_book'),
]