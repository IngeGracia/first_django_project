import uuid
from django.db import models
from django.urls import reverse



class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Ingrese el nombre del género (p. ej. Cientia Ficción, Poesía Francesa, etc.)')

    def __string__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Ingrese una breve descripción del libro')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Seleccione un género para este libro')

    def __str__(self):
        return self.title
    
    def get_aboslute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    


class BookInstance(models.Model):
    CHOICES_LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Avaialble'),
        ('r', 'Reserved'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para este libro particular en toda la biblioteca.')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=CHOICES_LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro.')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.book.title}'
    


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'