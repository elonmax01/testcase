from django.contrib import admin
from catalog.models import Author, Card, Review, Category, Post, Tag

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Card)
admin.site.register(Review)
# admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

