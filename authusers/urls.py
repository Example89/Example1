from django.contrib import admin
from django.urls import path, include

from authusers.views import index

# Прописывать базовый роутинг. Admin
urlpatterns = [
    path('', index, name='index'),

]   