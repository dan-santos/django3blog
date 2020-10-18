from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # dita para o django como a lista de posts (da pagina admin) devem ser exibidos
    # para aplica-lo, basta colocarmos como segundo argumento na hora de registrar o model
    # para ver mais, https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
    list_display = ['title', 'subtitle']

    # vai habilitar uma barra de busca na qual retornara para o usuario qualquer recorrencia da palavra buscada
    # nos campos listados na list
    search_fields = ['title', 'subtitle']

# Register your models here.
# Isto eh, sempre que quisermos que os models aparecam na pagina do admin, precisamos registra-los aqui, dessa forma:
admin.site.register(Post, PostAdmin)