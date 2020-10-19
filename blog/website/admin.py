from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    # dita para o django como a lista de posts (da pagina admin) devem ser exibidos
    # para aplica-lo, basta colocarmos como segundo argumento na hora de registrar o model
    # para ver mais, https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
    list_display = ['title', 'subtitle', 'categories', 'approved']

    # vai habilitar uma barra de busca na qual retornara para o usuario qualquer recorrencia da palavra buscada
    # nos campos listados na list
    search_fields = ['title', 'subtitle', 'categories']

    # Se soh quisermos mostrar determinados campos na tela de detalhe do post, digitamos o seguinte comando:
    # fields = ['title']

    # override do ModelAdmin
    # com essa funcao, podemos escolher o que mostrar na lista de posts, isto eh, definir condicioes para 
    # cada post para que o django mostre (ou nao) ele
    # def get_queryset(self, request):
        # soh ira listar os posts aprovados
        # return Post.objects.filter(approved=True)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email', 'message']

# Register your models here.
# Isto eh, sempre que quisermos que os models aparecam na pagina do admin, precisamos registra-los aqui, dessa forma:
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)