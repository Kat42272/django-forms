"""recipebox_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipe_app.views import index, recipe_detail, author_details, recipe_form_view, author_form_view

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>/', recipe_detail, name='recipes'),
    path('author/<int:author_id>/', author_details, name='authors'),
    path('newrecipe/', recipe_form_view, name='recipe_form'),
    path('newauthor/', author_form_view, name='author_form'),
    path('admin/', admin.site.urls),
]
