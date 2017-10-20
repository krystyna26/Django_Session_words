from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'processing', views.processing),   
    url(r'^clear$', views.clear),
]