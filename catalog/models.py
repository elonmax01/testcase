from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.urls import reverse
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name




class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    title_img = models.ImageField(upload_to='media/', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", blank=True, related_name="categories")
    tags = models.ManyToManyField("Tag", blank=True)


    def __str__(self):
        return self.title

    def get_next_id(self):
        is_next = Post.objects.filter(id=self.id+1).exists()
        while is_next is True:
            self.id = self.id + 1
        return self.id

    def get_previous_id(self):
        is_previous = Post.objects.filter(id=self.id-1).exists()
        if is_previous:
            return self.id - 1
        else:
            return self.id - 2

    def is_next(self):

        if self.id == Post.objects.last().id:
            return False

        is_next = Post.objects.filter(id=self.id+1).exists()
        return is_next





class Tag (models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name



class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    neuro_description = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=50, null=True, blank=True)
    thumb = ImageField(upload_to='media/')
    amount = models.IntegerField()



    icon_status = (('C', 'car'), ('F', 'foot'))
    gastronomy_status = (('y', 'yes'), ('n', 'no'))
    wine_status = (('y', 'yes'), ('n', 'no'))
    minskin_status = (('y', 'yes'), ('n', 'no'))

    icon = models.CharField(max_length=1, choices=icon_status, blank=True, default='C', help_text='На чем добираться?')
    gastronomy = models.CharField(max_length=1, choices=gastronomy_status, blank=True, default='n', help_text='Отметка для гастрономических маршрутов')
    wine = models.CharField(max_length=1, choices=wine_status, blank=True, default='n', help_text='Будет ли что выпить?')
    minskin = models.CharField(max_length=1, choices=minskin_status, blank=True, default='y', help_text='Маршрут внутригородской или с выездом за город?')



    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)

    def __str__(self):
        return self.title



