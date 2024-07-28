from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.getData),
    path('hello', views.hello),

    #path('post/', views.postData)
]
