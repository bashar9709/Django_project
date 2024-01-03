from django.urls import path
# from book.views import home, storebook, showBook, editBook, deleteBook
from . import views

urlpatterns = [
    # path('',views.home,),
    # path('',views.TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.Mytemplateview.as_view(template_name='home.html'), name='home'),
    # path('store_book/',views.storebook,name='storebook'),
    path('store_book/',views.BookFormView.as_view(),name='storebook'),
    # path('show_book/',views.showBook,name='showbook'),
    path('show_book/',views.BookListView.as_view(),name='showbook'),
    path('book_details/<int:id>',views.BookDetailsView.as_view(),name='details_book'),
    # path('edit_book/<int:id>',views.editBook,name='edit_book'),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name='edit_book'),
    # path('delete_book/<int:id>',views.deleteBook,name='delete_book'),
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(),name='delete_book'),
]