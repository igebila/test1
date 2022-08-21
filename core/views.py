from turtle import title
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
from django.db.models import Q


# Home Page View
class Home(ListView):
    template_name= 'index.html'
    model = Home

# About Page View
class About(ListView):
    template_name= 'aboutus.html'
    model = About

# Contact us Page View
class Contactus(ListView):
    template_name= 'contactus.html'
    model = Contactus
 
 #   Model For Book
class HomeView(ListView):
    model= Book
    paginate_by = 5
    ordering = "-timestamp"
    template_name= 'books.html'
 #   Model For Search   
class SearchResultsView(ListView):
    model = Book
    template_name = 'search_item.html'

    # def get_queryset(self): # new
    #     return Book.objects.filter(Q(title__icontains="q") | Q(state__icontains="NY")
    #     )

def dynamic_articles_view(request):
    Q['object_list'] = Book.objects.filter(title__icontains=request.GET.get('search'))
    return render(request, "search_item.html",Q)

# def Search(request):
#     if 'q' in request.GET:
#         q=request.GET['q']
#         Book = Book.objects.filter(title__icontains=q)
#         return render(request,'search_item.html', {'q':q})
#     else:
#          Book = Book.objects.all()  
#     return render(request,'search_item.html', {'q':q}, Book)  

def upload_file(request):
   context = {}
   if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        return render(request, 'books.html', context)

  
#   Model For Videos
class VideoView(ListView):
    model= Video
    paginate_by = 5
    ordering = "-timestamp"
    template_name= 'video-1.html'
    
def upload_video(request):
    video = Video.objects.all()
    context = {
        'video':video,
    }
    if request.method == 'POST':
            uploaded_video = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_video.name, uploaded_video)
            context['url'] = fs.url(name)
            return render(request, 'video-1.html', context)
    return render(request, 'video-1.html', context)
#   Model For News
class NewsView(ListView):
    model= News
    paginate_by = 3
    ordering = "-timestamp"
    template_name= 'news-1.html'

def upload_news(request):
    News = News.objects.all()
    context = {
        'news':News,
    }
    if request.method == 'POST':
            uploaded_news = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_news.name, uploaded_news)
            context['url'] = fs.url(name)
            return render(request, 'news-1.html', context)
    return render(request, 'news-1.html', context)