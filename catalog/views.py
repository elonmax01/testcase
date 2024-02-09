import datetime

from django.http import Http404
from django.shortcuts import render
from django.views import generic
from catalog.models import Author, Card, Review, Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
def index(request):
    num_authors = Author.objects.count()
    reviews = Review.objects.all()
    posts = Post.objects.all().order_by("-created_on")[:3]
    recent = Post.objects.all().order_by("-created_on")[:5]
    return render(
        request,
        'index.html',
        context=
        {
            'num_authors': num_authors,
            'reviews': reviews,
            'posts': posts,
            'recent': recent,
        },
    )

def elements(request):
    return render(request, 'elements.html', context={})

def about(request):
    reviews = Review.objects.all()
    posts = Post.objects.all().order_by("-created_on")[:3]
    recent = Post.objects.all().order_by("-created_on")[:5]
    return render(request, 'about.html', context={'reviews': reviews, 'posts': posts, 'recent': recent, })

def contact(request):
    recent = Post.objects.all().order_by("-created_on")[:5]
    return render(request, 'contact.html', context={'recent': recent, })

def tours(request):
    cards = Card.objects.all()
    cards_auto = Card.objects.filter(icon='C').count()
    cards_pesh = Card.objects.filter(icon='F').count()
    cards_minsk = Card.objects.filter(minskin='y').count()
    cards_outlook = Card.objects.filter(minskin='n').count()
    recent = Post.objects.all().order_by("-created_on")[:5]
    return render(request, 'tours.html', context={'cards': cards,
                                                  'cards_auto': cards_auto,
                                                  'cards_pesh': cards_pesh,
                                                  'cards_minsk': cards_minsk,
                                                  'cards_outlook': cards_outlook,
                                                  'recent': recent,})

def courses(request):
    reviews = Review.objects.all()
    return render(request, 'courses.html', context={'reviews': reviews})

def detail(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    reviews = Review.objects.all()
    return render(request, 'course_details.html', context={'reviews': reviews, "card": card})

def blog(request):
    post = Post.objects.all().order_by("-created_on")
    paginator = Paginator(post, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    recent = Post.objects.all().order_by("-created_on")[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    for tag in tags:
        tag.count = Post.objects.filter(tags__name__icontains=tag.name).count()
    return render(request, 'blog.html', context={'posts': posts, 'categories': categories, 'recent': recent, 'page': page, 'tags': tags, })

def single_blog(request, blog_id):
    try:
        post = Post.objects.get(pk=blog_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent = Post.objects.all().order_by("-created_on")[:5]
    for tag in tags:
        tag.count = Post.objects.filter(tags__name__icontains=tag.name).count()
    return render(request, 'single-blog.html', context={'post': post, 'categories': categories, 'recent': recent, 'tags': tags})

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
    if query == '':
        query = 'None'
    results = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(body__icontains=query)).order_by("-created_on")
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent = Post.objects.all().order_by("-created_on")[:5]

    for tag in tags:
        tag.count = Post.objects.filter(tags__name__icontains=tag.name).count()
    return render(request, 'search.html', {'query': query, 'results': results, 'posts': posts, 'page': page, 'categories': categories, 'tags': tags, 'recent': recent})

def category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Post.DoesNotExist:
        raise Http404("Post with this category does not exist")
    posts_in = Post.objects.filter(categories__name__icontains=category.name).order_by("-created_on")
    paginator = Paginator(posts_in, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', context={'category': category, 'posts': posts})

def tag(request, tag_id):
    try:
        single_tag = Tag.objects.get(pk=tag_id)
    except Post.DoesNotExist:
        raise Http404("Post with this tag does not exist")
    posts_in = Post.objects.filter(tags__name__icontains=single_tag.name).order_by("-created_on")
    paginator = Paginator(posts_in, 10)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    recent = Post.objects.all().order_by("-created_on")[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    for tag in tags:
        tag.count = Post.objects.filter(tags__name__icontains=tag.name).count()
    return render(request, 'blog.html', context={'single_tag': single_tag, 'posts': posts, 'recent': recent, 'categories': categories, 'tags': tags, })

def date(request, year, month, day):
    posts = Post.objects.filter(Q(created_on__year=year) & Q(created_on__month=month) & Q(created_on__day=day)).order_by("-created_on")

    recent = Post.objects.all().order_by("-created_on")[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    for tag in tags:
        tag.count = Post.objects.filter(tags__name__icontains=tag.name).count()
    return render(request, 'blog.html', context={'posts': posts, 'recent': recent, 'categories': categories, 'tags': tags})