from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index')
]