from django.db import models
from django.template.defaultfilters import slugify
from .utils import generateSlug

class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)


# Create your models here.
class Student(models.Model):
    gender_choices = (
        ('male','Male'),
        ('female','Female'),
    )
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender_choices, default='male')
    age = models.IntegerField(null = True, blank = True)
    student_bio = models.TextField()



class Author(models.Model):
    author_name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    price = models.IntegerField()
    published_date = models.DateField()

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default="IN", max_length=100)


class Products(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100, null= True, blank = True)

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = generateSlug(self.product_name, Products)
        return super().save(*args, **kwargs)

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=Student.gender_choices, default='male')
    upload_file = models.FileField(upload_to='files/', null=True, blank=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=1000)