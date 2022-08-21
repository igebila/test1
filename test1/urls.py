
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from core.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('home/', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
     path('contact/', Contactus.as_view(), name='contact'),
    path('books/', HomeView.as_view(), name='books'),
    path('video/', VideoView.as_view(), name='video'),
    path('news/', NewsView.as_view(), name='news'),
    path('search/', SearchResultsView.as_view(), name='search'),
    
    # path('books/',views.upload_file, name='upload_file'),
    #path('videos/',views.upload_video, name='upload_video'),
  
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()