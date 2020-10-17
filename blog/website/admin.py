from django.contrib import admin
from .models import Post

# Register your models here.
# Isto eh, sempre que quisermos que os models aparecam na pagina do admin, precisamos registra-los aqui, dessa forma:

admin.site.register(Post)