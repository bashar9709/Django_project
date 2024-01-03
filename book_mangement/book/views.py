from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import bookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# function based view
# def home(request):
#     return render(request, 'home.html')

# class based view
class Mytemplateview(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'Rahim','age':23}
        print(kwargs)
        context.update(kwargs) #dictionary uddate korear jonno update use kora
        return context

#funtion based view 
# def storebook(request):
#     if request.method == 'POST':
#         book = bookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
           
#             return redirect('showbook')
#         else:

#             book = bookStoreForm()
#     else:
#         book = bookStoreForm()
#     return render(request, 'store_book.html', {'form': book})

# class based view
# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = bookStoreForm
#     # success_url = reverse_lazy('showbook')
#     def form_valid(self, form):
#         form.save()
#         return redirect('showbook')
#(uporer class ar bikolpo)
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = bookStoreForm
    success_url = reverse_lazy('showbook')
    
    
    

# def showBook(request):
#     book = BookStoreModel.objects.all()
#     print(book)
    
#     return render(request,'show_book.html',{'data':book})


# class based view
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    
    # list query korar jonno
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id='3')
    
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'rakib':BookStoreModel.objects.all().order_by('author')}
    #     return context
    
    # ordering = ['-id']
    
    # def get_template_names(self): #template ke override korbe
    #     if self.request.user.is_superuser:
    #         template_name = 'superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'staffuser.html' 
    #     else:
    #         template_name = self.template_name
    #     return [template_name]           
       
# book_details korar jonno 
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'david'
    pk_url_kwarg = 'id'

# def editBook(request,id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = bookStoreForm(instance = book)
#     if request.method == 'POST':
#         form = bookStoreForm(request.POST,instance = book)
#         if form.is_valid():
#             form.save()
#             return redirect('showbook')
#     return render(request,'store_book.html',{'form':form})

# class based views
class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = bookStoreForm
    success_url = reverse_lazy('showbook')


# class based view
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('showbook')
    
# def deleteBook(request,id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     return redirect('showbook')
    