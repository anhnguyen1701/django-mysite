from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.post),
    path('2/', views.post2)
]
