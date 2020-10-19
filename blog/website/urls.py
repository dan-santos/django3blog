from django.urls import path, include
from .views import hello_blog, post_detail

# imports necessarios para a adicao de media nos posts
# (adicao feita no fim da lista urlpatterns)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', hello_blog, name='home_blog'), # url vazia eh equivalente a home deste app
    # post detalhado
    # Sera chamada pelo nome no template index.html
    path('post/<int:id>/', post_detail, name='post_detail'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)