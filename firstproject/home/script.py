import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()


from models import Author, Book

def handle():
    book_count = Book.objects.count()
    print(book_count)

handle()
