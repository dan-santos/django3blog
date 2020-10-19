"""blog URL Configuration

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
from django.urls import path, include
from .views import hello_world

# imports necessarios para a adicao de media nos posts
# (adicao feita no fim da lista urlpatterns)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # toda url precisa estar necessariamente linkada com uma view
    # o include linka o endereco url com uma serie de outras urls de um app especifico
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('blog/', include('website.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
