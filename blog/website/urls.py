from django.urls import path, include
from .views import hello_blog, post_detail, save_form

urlpatterns = [
    path('', hello_blog, name='home_blog'), # url vazia eh equivalente a home deste app
    # post detalhado
    # Sera chamada pelo nome no template index.html
    path('post/<int:id>/', post_detail, name='post_detail'), 
    path('save-form', save_form, name='save_form'),
]