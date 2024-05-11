from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-homepage'),
    path('misc/990scraper', views.scraper, name='portfolio-homepage-990scraper'),
]
