from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    })


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        queryset = Book.objects.filter(title__icontains="war")[:5] # Consigue 5 libros que contengan el título de guerra.

    def get_context_data(self):
        # Llamar a la implementación base para obtener un contexto
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'Estos son solo algunos datos.'
        return context