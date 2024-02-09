from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('elements/', views.elements, name='elements'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tours/', views.tours, name='tours'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.single_blog, name='post'),
    path('blog/search', views.search, name='search'),
    path('blog/category/<int:category_id>', views.category, name='category'),
    path('blog/date/<int:year>/<int:month>/<int:day>', views.date, name='date'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:card_id>', views.detail, name='details'),
    path('blog/tag/<int:tag_id>', views.tag, name='tags')
]